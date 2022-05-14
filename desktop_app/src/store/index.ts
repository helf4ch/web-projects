import { createStore } from "vuex";
import { playingModule } from "@/store/playingModule";

export default createStore({
  modules: {
    player: playingModule,
  },
});
