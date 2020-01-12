<template>
  <div class="board-cell">
    <img src="../assets/cell.png" width="20px" height="20px" />
  </div>
</template>

<script>
export default {
  name: "Cell",
  props: {
    msg: String
  }
};
</script>

<style scoped>
.board-cell{
  background: red;
  max-width: 20px;
  max-height: 20px;
  
}
img {
  /* text-align: center; */
  /* display: block; */
}
</style>