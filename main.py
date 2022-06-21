# idk where they were hiding this absorb function but it needs to go somewhere
# and it wasn't in the meme, so i can't put it after the import. it goes here now
def absorb(water):
    print( '\n----------------')
    water['observe_moisture']()
    water['release_moisture']()
    water['observe_moisture']()
    print('----------------')

# code from foot mat
import foot

for n in foot:
    if foot[n].water is None:
        continue
    else:
        absorb(foot[n].water)
