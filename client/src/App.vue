<template>
  <div id="app">
    <button @click="confirm">confirm</button>
    <button @click="cancel" :disabled="this.playedCells.length == 0">cancel</button>
    <Board @cellClicked="cellClicked" :selectedCells="this.playedCells" />
  </div>
</template>

<script>
import Board from "./components/Board.vue";

export default {
  name: "app",
  components: {
    Board
  },
  methods: {
    /* eslint-disable no-console */
    confirm() {
      console.log("confirm with values", this.playedCells);
      this.playedCells = [];
    },
    cancel() {
      this.playedCells = [];
    },
    cellClicked(id) {
      if (!this.playedCells.includes(id)) {
        if (this.playedCells.length < 2) {
          this.playedCells.push(id);
        } else {
          alert(
            "You can't play more than 2 cells. Click cancel to play other cells."
          );
        }
      }
    }
  },
  data() {
    return {
      playedCells: [],
      selectedCells: []
    };
  }
};
</script>

<style>
html {
  background-image: url("assets/bg.png");
  background-size: cover;
  background-repeat: no-repeat;
}

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
