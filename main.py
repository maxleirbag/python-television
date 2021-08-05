import sys

from energy import Energy
from channel import Channel
from volume import Volume


class Television:
    power = True
    channel = 2
    volume = 10
    command = 'unsatisfied'
    options_on = """\nAction: Description
    up: turn up the volume
    down: turn down the volume
    next: go to the immediately higher available channel
    previous: go to the immediately lower available channel
    off: turn off the TV
    """
    options_off = """
    on: turn on the TV again
    drop: finally drop the remote and forget about the TV
    """

    def use(self):

        print("\n*** TV turned on ***")

        while self.command != 'off':
            print(self.options_on)
            self.command = input("What command do you wish for the TV to execute? ").lower()

            if self.command == 'off':
                Energy.energize(Television)
            else:
                if self.command == 'next':
                    Channel.change_channel(Television, 'next', self.channel)
                elif self.command == 'previous':
                    Channel.change_channel(Television, 'previous', self.channel)

                elif self.command == 'up':
                    Volume.change_volume(Television, 'up', self.volume)
                    self.volume += 1
                elif self.command == 'down':
                    Volume.change_volume(Television, 'down', Television.volume)
                    self.volume -= 1

        print(self.options_off)
        self.command = input("What do you choose? ")
        if self.command == 'on':
            self.use(Television)
        else:
            print("Bye")
            sys.exit()


Television.use(Television)
