<template>
  <player-button>
    <prev-button-icon @click="this.prevTrack"></prev-button-icon>
  </player-button>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import PrevButtonIcon from "@/components/UI/icons/PrevButtonIcon.vue";
import { mapMutations } from "vuex";

export default defineComponent({
  components: {
    PrevButtonIcon,
  },
  methods: {
    ...mapMutations({
      prevTrack: "player/prevTrack",
    }),
  },
});
</script>

<style></style>
