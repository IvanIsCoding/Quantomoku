<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png" width="300px"/>
    <Board />
  </div>
</template>

<script>
import Board from "./components/Board.vue";

export default {
  name: "app",
  components: {
    Board
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
