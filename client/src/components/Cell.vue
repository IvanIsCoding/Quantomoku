<template>
  <div class="board-cell">
    <img
      v-if="this.value == 'n'"
      src="../assets/P1.png"
      width="40px"
      height="40px"
      @click="clicked"
      :class="this.selected? 'selected' : ''"
    />
    <img
      v-else-if="this.value=='x'"
      src="../assets/red_placeholder.png"
      width="40px"
      height="40px"
      @click="clicked"
      :class="this.selected? 'selected' : ''"
    />
    <img
      v-else-if="this.value=='o'"
      src="../assets/blue_placeholder.png"
      width="40px"
      height="40px"
      @click="clicked"
      :class="this.selected? 'selected' : ''"
    />
    <!-- <span style="margin-right: 10px">{{id}}</span> -->
  </div>
</template>

<script>
export default {
  name: "Cell",
  props: {
    id: String,
    selected: Boolean,
    value: String
  },
  data() {
    return {
      // selected: false
    };
  },
  methods: {
    clicked() {
      this.$emit("cellClicked", this.id);
    }
  }
};
</script>

<style scoped>
.board-cell {
  max-width: 40px;
  max-height: 40px;
}
img {
  /* text-align: center; */
  /* display: block; */
  opacity: 0.5;
}
.selected {
  opacity: 1;
}
</style>