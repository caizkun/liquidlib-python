from liquidlib.trajectory import TrrTrajectory, XtcTrajectory, XyzTrajectory, LammpsTrajectory


class TrajectoryFactory(object):
    """ This is a simple factory to prepare trajectory. """

    def __init__(self):
        pass

    def create_trajectory(self, trajectory_file_name):
        trajectory_file_type = str(trajectory_file_name).split(".")[-1]

        if trajectory_file_type == "trr":
            return TrrTrajectory()
        elif trajectory_file_type == "xtc":
            return XtcTrajectory()
        elif trajectory_file_type == "xyz":
            return XyzTrajectory()

        return None


class DemoCustomizedTrajectoryFactory(TrajectoryFactory):
    """ This is a demo class to extend TrajectoryFactory """
    def create_trajectory(self, trajectory_file_name):
        trajectory = super().create_trajectory(trajectory_file_name)

        if trajectory is None:
            trajectory_file_type = str(trajectory_file_name).split(".")[-1]

            if trajectory_file_type == "lammpstrj":
                trajectory = LammpsTrajectory()

        return trajectory


# class TrajectoryFactory(object):
#     """ This is a simple factory to prepare trajectory. """
#
#     def __init__(self):
#         pass
#
#     def read_trajectory(self, input_parameters):
#         trajectory_file_type = input_parameters["trajectory_file_name"].split(".")[-1]
#
#         if trajectory_file_type == "trr":
#             return self._read_trr_file(input_parameters)
#         elif trajectory_file_type == "xtc":
#             return self._read_xtc_file(input_parameters)
#         elif trajectory_file_type == "xyz":
#             return self._read_xyz_file(input_parameters)
#
#         # TODO: how to cooperate with InputChecker() for unrecognized type
#         return None
#
#
#     def _read_trr_file(self, input_parameters):
#         """ This method reads .trr file. """
#         trajectory = Trajectory()
#         return trajectory
#
#     def _read_xtc_file(self, input_parameters):
#         """ This method reads .xtc file. """
#         pass
#
#     def _read_xyz_file(self, input_parameters):
#         """ This method reads .xyz file. """
#         pass
#
#     # add more types, or inherit to extend


# class DemoExtendedTrajectoryFactory(TrajectoryFactory):
#     """ This is a demo class to extend TrajectoryFactory """
#
#     def read_trajectory(self, input_parameters):
#         super().read_trajectory()
#
#         trajectory_file_type = input_parameters["trajectory_file_name"].split(".")[-1]
#         if trajectory_file_type == 'lammpstrj':
#             return self._read_lammpstrj_file(input_parameters)
#
#         # TODO: how to register new factory for use
#
#     def _read_lammpstrj_file(self, input_parameters):
#         """ This method reads .lammpstrj file. """
#         pass