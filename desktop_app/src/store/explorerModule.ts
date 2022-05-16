export const explorerModule = {
  state: () => ({
    currentPath: "",
    prevPath: "",
    files: [],
    isExplorerActive: false,
  }),
  mutations: {
    setAppPath(state, path) {
      state.prevPath = state.currentPath;
      state.currentPath = path;
    },
    setFilesArray(state, files) {
      state.files = files;
    },
    changeExplorerActive(state) {
      state.isExplorerActive = !state.isExplorerActive;
    },
    goToPrevPath(state) {
      if (state.prevPath === "") {
        return;
      }
      const tmp = state.prevPath;
      state.prevPath = state.currentPath;
      state.currentPath = tmp;
    },
  },
  namespaced: true,
};
