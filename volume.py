class Volume:

    def change_volume(self, command_volume, current_volume):

        if command_volume == 'up':
            current_volume += 1
        elif command_volume == 'down':
            current_volume -= 1
        print("Volume: ", current_volume)

        return current_volume