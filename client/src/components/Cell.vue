<template>
  <div class="board-cell">
    <img src="../assets/P1.png" width="40px" height="40px" />
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
  
  max-width: 40px;
  max-height: 40px;
  
}
img {
  /* text-align: center; */
  /* display: block; */
}
</style>