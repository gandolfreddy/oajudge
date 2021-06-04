# That's RIGHT

# input
bed_mmss = list(map(int, input().split(":")))
wake_mmss = list(map(int, input().split(":")))

# process
mid_t = 23*60 + 59
bed_t = bed_mmss[0]*60 + bed_mmss[1]
wake_t = wake_mmss[0]*60 + wake_mmss[1]
if not wake_t:
    mid_t += 1
total_t = mid_t-bed_t+wake_t if bed_t > wake_t else wake_t-bed_t

m = total_t // 60
s = total_t % 60
m = f"0{m}" if m < 10 else f"{m}"
s = f"0{s}" if s < 10 else f"{s}"
result = f"{m}:{s}"

# output
print(result)
