<template>
  <div class="board-cell" width="20px" height="20px">
    <img
      :src="require( `../assets/${this.assetPath}`)"
      width="40px"
      height="40px"
      @click="clicked"
      :class="this.selected? 'selected' : ''"
    />
    <!-- <span style="margin-right: 10px; font-size:5px">{{id}}</span> -->
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
  methods: {
    clicked() {
      this.$emit("cellClicked", this.id);
    }
  },
  computed: {
    assetPath() {
      var result = "P1";
      switch (this.value) {
        case "n":
          result = "neutral.png";
          break;
        case "x":
          result = "P1.png";
          break;
        case "o":
          result = "P2.png";
          break;
        case "q_0":
          result = "Ent_B.gif";
          break;
        case "q_1":
          result = "Ent_G.gif";
          break;
        case "q_2":
          result = "Ent_P.gif";
          break;
        case "q_3":
          result = "Ent_R.gif";
          break;
        case "q_4":
          result = "Ent_Y.gif";
          break;
      }
      return result;
    }
  }
};
</script>

<style scoped>
.board-cell {
  background: rgba(255, 164, 80, 0.2);
  
  margin:1.5px;
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