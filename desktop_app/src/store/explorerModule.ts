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
  },
  namespaced: true,
};
