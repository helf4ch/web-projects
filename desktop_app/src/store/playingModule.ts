export const playingModule = {
  state: () => ({
    pathToTrackList: "",
    isPlaying: false,
    trackList: [],
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
    },
    setTrackIndex(state, index) {
      if (index >= state.trackList.length) {
        state.trackIndex = 0;
      } else {
        state.trackIndex = index;
      }
    },
    nextTrack(state) {
      if (state.trackIndex >= state.trackList.length - 1) {
        state.trackIndex = 0;
      } else {
        state.trackIndex += 1;
      }
    },
    prevTrack(state) {
      if (state.trackIndex <= 0) {
        state.trackIndex = state.trackList.length - 1;
      } else {
        state.trackIndex -= 1;
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
      state.trackIndex = 0;
    },
  },
  actions: {
    onEnd({ commit, state }) {
      if (state.repeatType.repeatFolder) {
        commit("nextTrack");
      }
      if (
        state.repeatType.repeatOff &&
        state.trackIndex != state.trackList.length - 1
      ) {
        commit("nextTrack");
      }
    },
  },
  namespaced: true,
};
