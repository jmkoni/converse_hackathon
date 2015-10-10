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
        self.gyroscope = None
        self.acceleration = None
        self.last_time = 0

    def output(self, myo):
        
        ctime = time.time()
        if (ctime - self.last_time) < self.interval:
            return
        self.last_time = ctime
        parts = []
        # parts = [orientation.x, orientation.y, orientation.z, orientation.w, pose, emg1, emg2, emg3, emg4, emg5, emg6, emg7, emg8, gyro1, gyro2, gyro3, accel1, accel2, accel3]
        
        if self.orientation:
            for comp in self.orientation:
                parts.append(str(comp))
        parts.append(str(self.pose.name))
        if self.emg:
            for comp in self.emg:
                parts.append(str(comp))
        if self.gyroscope:
            for comp in self.gyroscope:
                parts.append(str(comp))
        if self.acceleration:
            for comp in self.acceleration:
                parts.append(str(comp))
        end_line = '\r[' + str(myo.value) + ',' + ','.join(parts) + "]"
        global client
        msg = osc_message_builder.OscMessageBuilder(address = "/data_{}".format(myo.value))
        msg.add_arg(end_line)
        msg = msg.build()
        client.send(msg)
        print(end_line)
        sys.stdout.flush()

    def on_connect(self, myo, timestamp, firmware_version):
        global msg
        myo.vibrate('short')
        myo.vibrate('short')
        myo.request_battery_level()
        myo.set_stream_emg(libmyo.StreamEmg.enabled)
        self.emg_enabled = True

    def on_pose(self, myo, timestamp, pose):
        # maybe we want special functionality depending on a pose?
        self.pose = pose
        self.output(myo)

    def on_orientation_data(self, myo, timestamp, orientation):
        self.orientation = orientation
        self.output(myo)

    def on_accelerometor_data(self, myo, timestamp, acceleration):
        self.acceleration = acceleration
        self.output(myo)

    def on_gyroscope_data(self, myo, timestamp, gyroscope):
        self.gyroscope = gyroscope
        self.output(myo)

    def on_emg_data(self, myo, timestamp, emg):
        self.emg = emg
        self.output(myo)

    def on_unlock(self, myo, timestamp):
        self.locked = False
        self.output(myo)

    def on_lock(self, myo, timestamp):
        self.locked = True
        self.output(myo)

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
    global client
    client = udp_client.UDPClient('127.0.0.1', 8000)
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
