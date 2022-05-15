import { createStore } from "vuex";
import { playingModule } from "@/store/playingModule";
import { explorerModule } from "@/store/explorerModule";

export default createStore({
  modules: {
    player: playingModule,
    explorer: explorerModule,
  },
});
