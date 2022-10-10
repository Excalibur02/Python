import speedtest as speed_test

def format_bytes(size):
    # 2**10 = 1024
    power = 2**10
    n = 0
    power_labels = {0 : 'Blocks', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}
    while size > power:
        size /= power
        n += 1
    return round(size,2)

test = speed_test.Speedtest()
test.get_servers()
# best = test.get_best_server()
#
# print(best['host'])

up_speed = test.upload()
down_speed = test.download()

print(f"Upload Speed : {format_bytes(up_speed)} MB")
print(f"Download Speed : {format_bytes(down_speed)} MB")

