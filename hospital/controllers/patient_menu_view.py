from controllers.controller import MainController
class PatientMenu:
    @staticmethod
    def show_options():
        MENU = {
            1: MainController.show_all_doctors,
            2: MainController.find_doctor_by_name,
            3: MainController.reserve_hour_for_certain_doctor,
            4: MainController.cancel_hour
        }