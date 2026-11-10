total_second=9875
hour = total_second // 3600
minutes = (total_second % 3600) // 60
seconds = total_second % 60
print(f"{total_second} seconds = {hour}h {minutes}min {seconds}s")
#testing if it true
print("Check: ",2*3600 + 44*60+35 == total_second)