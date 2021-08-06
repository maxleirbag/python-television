class Channel:
    channels = [2, 4, 5, 7, 9, 12]
    n = 0

    def change_channel(self,command_channel, current_channel):

        if command_channel == 'next':
            if Channel.n + 1 == len(Channel.channels):
                Channel.n = 0
                current_channel = Channel.channels[Channel.n]
            else:
                Channel.n += 1
                current_channel = Channel.channels[Channel.n]

        elif command_channel == 'previous':
            if Channel.n - 1 == -1:
                Channel.n = len(Channel.channels) - 1
                current_channel = Channel.channels[Channel.n]
            else:
                Channel.n -= 1
                current_channel = Channel.channels[Channel.n]

        elif command_channel == 'that':
            print(Channel.channels)
            Channel.n = int(input("Select one of the available channels: "))
            if Channel.n in Channel.channels:
                current_channel = Channel.n

        print("Channel: ", current_channel)

        return current_channel
