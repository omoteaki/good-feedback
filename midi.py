import mido

midi = mido.MidiFile("hands.mid")

midi.print_tracks(meta_only=True)

list = []

for tr in midi.tracks[0]:
  msg = tr.dict()
  if msg["type"] == "marker":
    time = msg["time"]
    marker = msg["text"]
    list.append({"time":time, "marker":marker})
    # print(f"{msg["text"]}\t:{msg["time"]}")

# print(list)

sum = 0
for li in list:
  sum += li["time"]
  second = sum / 29120
  li.update(time=second)
  # print(sum)


# for li, time in zip(list, sum):
for li in list:
  print(f"{li},")