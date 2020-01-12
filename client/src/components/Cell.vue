<template>
  <div class="board-cell">
    <img src="../assets/P1.png" width="40px" height="40px" @click="clicked" :class="this.selected? 'selected' : ''" />
  </div>
</template>

<script>
export default {
  name: "Cell",
  props: {
    id: String, 
    selected: Boolean
  },
  data() {
    return {
      // selected: false
    }
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