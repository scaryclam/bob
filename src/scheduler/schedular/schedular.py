class Schedular:
    def start(self, schedule):
        # Read the config for things to schedule
        for job in schedule:
            print(f'{job["name"]} - {job["message"]}')
