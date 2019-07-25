from viewer import PlotDiar

speakerSlice={'1': [{'start':175*100, 'stop':200}, {'start':30, 'stop':120}], '2': [{'start':90, 'stop':130*1000}]}
p = PlotDiar(map=speakerSlice, wav=r'example.wav', gui=True, size=(25, 6))
p.draw()
p.plot.show()