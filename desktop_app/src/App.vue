<template>
  <player-app></player-app>
  <!-- <div>
    <audio controls>
      <source
        src="file:///home/helf4ch/Музыка/Rammstein_-_Mein_Herz_brennt.mp3"
        type="audio/mpeg"
      />
    </audio>
  </div> -->
  <div class="explorer"></div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

import PlayerApp from "@/components/player/PlayerApp.vue";
import { getFilesAndTracks } from "@/hooks/getFilesAndTracks";
import { mapMutations } from "vuex";

export default defineComponent({
  components: {
    PlayerApp,
  },
  setup() {
    const { path, files, trackList } = getFilesAndTracks();

    return {
      path,
      files,
      trackList,
    };
  },
  methods: {
    ...mapMutations({
      setTrackList: "player/setTrackList",
    }),
  },
  created() {
    this.setTrackList(this.trackList);
  },
});
</script>

<style>
body {
  background-color: #282828;
  color: #ebdbb2;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
</style>
