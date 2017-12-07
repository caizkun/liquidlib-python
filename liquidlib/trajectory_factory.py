class TrajectoryFactory(object):
    """ Abstract factory for build trajectory """

    def __init__(self, trjectory_file_name="traj.trr"):
        self._buildTrajectory(trjectory_file_name)


    def prepareTrajectory(self):
        return


class TrrTrajectoryFactory(TrajectoryFactory):
    """ factory to build .trr trajectory """

    def __init__(self):
        pass

    def prepareTrajectory(self):
        pass