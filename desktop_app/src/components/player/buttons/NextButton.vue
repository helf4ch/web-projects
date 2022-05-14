<template>
  <player-button>
    <next-button-icon @click="this.nextTrack"></next-button-icon>
  </player-button>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import NextButtonIcon from "@/components/UI/icons/NextButtonIcon.vue";
import { mapMutations } from "vuex";

export default defineComponent({
  components: {
    NextButtonIcon,
  },
  methods: {
    ...mapMutations({
      nextTrack: "player/nextTrack",
    }),
  },
});
</script>

<style></style>
