function shuffle(array) {
  let currentIndex = array.length,
    randomIndex;

  while (currentIndex != 0) {
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;

    [array[currentIndex], array[randomIndex]] = [
      array[randomIndex],
      array[currentIndex],
    ];
  }

  return array;
}

export const playingModule = {
  state: () => ({
    isShuffleTurnOn: false,
    isEqualiserTurnOn: false,
    isEqualiserShown: false,
    pathToTrackList: "",
    isPlaying: false,
    trackList: [],
    shuffleList: [],
    trackIndex: 0,
    repeatType: {
      repeatTrack: true,
      repeatFolder: false,
      repeatOff: false,
    },
  }),
  mutations: {
    playPauseTrack(state) {
      if (state.isPlaying) {
        state.isPlaying = false;
      } else {
        state.isPlaying = true;
      }
    },
    setPathToTrackList(state, path) {
      state.pathToTrackList = path;
    },
    setTrackList(state, trackList) {
      state.trackList = trackList;
      state.shuffleList = [];
      for (let i = 0; i < trackList.length; ++i) {
        state.shuffleList.push(i);
      }
    },
    setTrackIndex(state, index) {
      if (index >= state.trackList.length) {
        state.trackIndex = 0;
      } else {
        state.trackIndex = index;
      }
    },
    nextTrack(state) {
      if (
        state.shuffleList.indexOf(state.trackIndex) >=
        state.trackList.length - 1
      ) {
        state.trackIndex = state.shuffleList[0];
      } else {
        state.trackIndex =
          state.shuffleList[state.shuffleList.indexOf(state.trackIndex) + 1];
      }
    },
    prevTrack(state) {
      if (state.shuffleList.indexOf(state.trackIndex) <= 0) {
        state.trackIndex = state.shuffleList[state.trackList.length - 1];
      } else {
        state.trackIndex =
          state.shuffleList[state.shuffleList.indexOf(state.trackIndex) - 1];
      }
    },
    switchRepeat(state) {
      if (state.repeatType.repeatTrack) {
        state.repeatType.repeatTrack = false;
        state.repeatType.repeatFolder = true;
      } else if (state.repeatType.repeatFolder) {
        state.repeatType.repeatFolder = false;
        state.repeatType.repeatOff = true;
      } else if (state.repeatType.repeatOff) {
        state.repeatType.repeatOff = false;
        state.repeatType.repeatTrack = true;
      }
    },
    reloadPlayer(state) {
      state.isPlaying = false;
      state.trackIndex = state.shuffleList[0];
    },
    switchEqualiserOnAndOf(state) {
      state.isEqualiserTurnOn = !state.isEqualiserTurnOn;
    },
    switchEqualiserShown(state) {
      state.isEqualiserShown = !state.isEqualiserShown;
    },
    switchShuffleOnAndOf(state) {
      state.isShuffleTurnOn = !state.isShuffleTurnOn;
    },
    shuffleTrackList(state) {
      state.shuffleList = shuffle(state.shuffleList);
    },
    unshuffleTrackList(state) {
      state.shuffleList = [];
      for (let i = 0; i < state.trackList.length; ++i) {
        state.shuffleList.push(i);
      }
    },
  },
  actions: {
    onEnd({ commit, state }) {
      if (state.repeatType.repeatFolder) {
        commit("nextTrack");
      }
      if (
        state.repeatType.repeatOff &&
        state.shuffleList.indexOf(state.trackIndex) !=
          state.trackList.length - 1
      ) {
        commit("nextTrack");
      }
    },
  },
  namespaced: true,
};
