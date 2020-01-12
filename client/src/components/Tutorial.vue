<template>
  <div class="main">
    <div class="tutorial" v-if="currentPage == 1">
      Welcome
      <img src="../assets/Tutorial/1.png" />
    </div>
    <div class="tutorial" v-if="currentPage == 2">
      The Game
      <img src="../assets/Tutorial/2.png" />
    </div>
    <div class="tutorial" v-if="currentPage == 3">
      The Game
      <img src="../assets/Tutorial/3.png" />
    </div>
    <div class="tutorial" v-if="currentPage == 4">
      <img src="../assets/Tutorial/4.png" />
    </div>
    <div class="tutorial" v-if="currentPage == 5">
      <img src="../assets/Tutorial/5.png" />
    </div>
    <div class="tutorial" v-if="currentPage == 6">
      <img src="../assets/Tutorial/6.png" />
    </div>
    <button
      :class="currentPage == 1? 'forceNoHoverAnimation pageNav' : 'pageNav'"
      :disabled="currentPage == 1"
      @click="previousPage"
    >previous page</button>
    <button
      :class="currentPage == numberPages? 'forceNoHoverAnimation pageNav' : 'pageNav'"
      :disabled="currentPage == numberPages"
      @click="nextPage"
    >next page</button>
  </div>
</template>

<script>
export default {
  name: "Tutorial",
  data() {
    return {
      currentPage: 1,
      numberPages: 6
    };
  },
  methods: {
    nextPage() {
      this.currentPage++;
    },
    previousPage() {
      this.currentPage--;
    }
  }
};
</script>

<style scoped>
.main {
  width: 760px;
  display: block;
  margin: auto;
  padding: 20px;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  background-image: url("../assets/board.png");
}

.tutorial img {
  width: 100%;
}

.pageNav {
  display: inline-block;
}

.forceNoHoverAnimation {
  background: url("../assets/button_2.gif") 0 0 no-repeat !important;
}
</style>