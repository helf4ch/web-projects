export const explorerModule = {
  state: () => ({
    path: "",
    files: [],
  }),
  mutations: {
    setAppPath(state, path) {
      state.path = path;
    },
    setFilesArray(state, files) {
      state.files = files;
    },
  },
  namespaced: true,
};
