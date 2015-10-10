from __future__ import print_function
from pythonosc import osc_message_builder
from pythonosc import udp_client

import myo as libmyo; libmyo.init()
import time
import sys


class Listener(libmyo.DeviceListener):
    """
    Listener implementation. Return False from any function to
    stop the Hub.
    """

    interval = 0.05  # Output only 0.05 seconds

    def __init__(self):
        super(Listener, self).__init__()
        self.orientation = None
        self.pose = libmyo.Pose.rest
        self.emg_enabled = True
        self.locked = False
        self.rssi = None
        self.emg = None
        self.last_time = 0

    def output(self):
        client = udp_client.UDPClient('127.0.0.1', 8000)
        msg = osc_message_builder.OscMessageBuilder(address = '/data')
        ctime = time.time()
        if (ctime - self.last_time) < self.interval:
            return
        self.last_time = ctime

        parts = []
        # [0.64031982421875][0.06585693359375][-0.08184814453125][-0.76092529296875][<Pose: rest>][ ][ ][-60][9    ][-4   ][-12  ][-40  ][3    ][-1   ][-12  ][-54  ]

        # parts = [orientation.x, orientation.y, orientation.z, orientation.w, pose, emg1, emg2, emg3, emg4, emg5, emg6, emg7, emg8]
        if self.orientation:
            for comp in self.orientation:
                parts.append(str(comp).ljust(15))
        parts.append(str(self.pose.name).ljust(10))
        if self.emg:
            for comp in self.emg:
                parts.append(str(comp).ljust(5))
        end_line = '\r' + ','.join(parts) + ""
        msg.add_arg(end_line)
        msg = msg.build()
        client.send(msg)
        print(end_line.replace(" ", ""))
        sys.stdout.flush()

    def on_connect(self, myo, timestamp, firmware_version):
        myo.vibrate('short')
        myo.vibrate('short')
        myo.request_battery_level()

    def on_pose(self, myo, timestamp, pose):
        # maybe we want special functionality depending on a pose?
        # if pose == libmyo.Pose.double_tap:
        #     myo.set_stream_emg(libmyo.StreamEmg.enabled)
        #     self.emg_enabled = True
        # elif pose == libmyo.Pose.fingers_spread:
        #     myo.set_stream_emg(libmyo.StreamEmg.disabled)
        #     self.emg_enabled = False
        #     self.emg = None
        # self.pose = pose
        self.output()

    def on_orientation_data(self, myo, timestamp, orientation):
        self.orientation = orientation
        self.output()

    def on_accelerometor_data(self, myo, timestamp, acceleration):
        pass

    def on_gyroscope_data(self, myo, timestamp, gyroscope):
        pass

    def on_emg_data(self, myo, timestamp, emg):
        self.emg = emg
        self.output()

    def on_unlock(self, myo, timestamp):
        self.locked = False
        self.output()

    def on_lock(self, myo, timestamp):
        self.locked = True
        self.output()

    def on_event(self, kind, event):
        """
        Called before any of the event callbacks.
        """

    def on_event_finished(self, kind, event):
        """
        Called after the respective event callbacks have been
        invoked. This method is *always* triggered, even if one of
        the callbacks requested the stop of the Hub.
        """

    def on_pair(self, myo, timestamp, firmware_version):
        """
        Called when a Myo armband is paired.
        """

    def on_unpair(self, myo, timestamp):
        """
        Called when a Myo armband is unpaired.
        """

    def on_disconnect(self, myo, timestamp):
        """
        Called when a Myo is disconnected.
        """

    def on_arm_sync(self, myo, timestamp, arm, x_direction, rotation,
                    warmup_state):
        """
        Called when a Myo armband and an arm is synced.
        """

    def on_arm_unsync(self, myo, timestamp):
        """
        Called when a Myo armband and an arm is unsynced.
        """

    def on_battery_level_received(self, myo, timestamp, level):
        """
        Called when the requested battery level received.
        """

    def on_warmup_completed(self, myo, timestamp, warmup_result):
        """
        Called when the warmup completed.
        """


def main():
    print("Connecting to Myo ... Use CTRL^C to exit.")
    try:
        hub = libmyo.Hub()
    except MemoryError:
        print("Myo Hub could not be created. Make sure Myo Connect is running.")
        return

    hub.set_locking_policy(libmyo.LockingPolicy.none)
    hub.run(1000, Listener())

    # Listen to keyboard interrupts and stop the hub in that case.
    try:
        while hub.running:
            time.sleep(0.25)
    except KeyboardInterrupt:
        print("\nQuitting ...")
    finally:
        print("Shutting down hub...")
        hub.shutdown()


if __name__ == '__main__':
    main()
