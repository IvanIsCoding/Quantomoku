<template>
  <div class="board-cell">
    <img
      :src="require( `../assets/${this.assetPath}`)"
      width="45px"
      height="45px"
      @click="clicked"
      :class="this.selected? 'selected' : '' + (this.collapsed? ' collapsed' : '')"
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
        case ">_0":
          result = "P1sup_B.gif";
          break;
        case ">_1":
          result = "P1sup_G.gif";
          break;
        case ">_2":
          result = "P1sup_P.gif";
          break;
        case ">_3":
          result = "P1sup_R.gif";
          break;
        case ">_4":
          result = "P1sup_Y.gif";
          break;
        case "(_0":
          result = "P2sup_B.gif";
          break;
        case "(_1":
          result = "P2sup_G.gif";
          break;
        case "(_2":
          result = "P2sup_P.gif";
          break;
        case "(_3":
          result = "P2sup_R.gif";
          break;
        case "(_4":
          result = "P2sup_Y.gif";
          break;
        case "x_0":
        case "x_1":
        case "x_2":
        case "x_3":
        case "x_4":
          result = "P1_nc.gif";
          break;
        case "o_0":
        case "o_1":
        case "o_2":
        case "o_3":
        case "o_4":
          result = "P2_nc.gif";
          break;
      }
      return result;
    },
    collapsed() {
      return this.assetPath == "P1.png" || this.assetPath == "P2.png";
    }
  }
};
</script>

<style scoped>
.board-cell {
  background: rgba(255, 164, 80, 0.2);

  padding: 2px;
  margin: 1.5px;
  max-width: 45px;
  max-height: 45px;
}
img {
  /* text-align: center; */
  /* display: block; */
  opacity: 0.5;
}
.selected-x {
  opacity: 1;
}
.selected-o {
  opacity: 1;
}
.collapsed {
  opacity: 1;
}
</style>