export const explorerModule = {
  state: () => ({
    currentPath: "",
    prevPath: "",
    files: [],
  }),
  mutations: {
    setAppPath(state, path) {
      state.prevPath = state.currentPath;
      state.currentPath = path;
    },
    setFilesArray(state, files) {
      state.files = files;
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
