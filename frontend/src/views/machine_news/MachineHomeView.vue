<template>
  <div class="machine-news-container">
    <h1>Welcome to machine news!</h1>
  </div>
</template>

<script>
import { onMounted } from 'vue'
import stateSite from '@/modules/site'
export default {
  setup() {
    const { setSite } = stateSite

    onMounted(() => {
      setSite('machine_news')
    })
  }
}
</script>

<style scoped>
.machine-news-container{
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
}
.header{
  grid-column: 1 / 4;
  grid-row: 1;
}
.create-machine-modal {
  position: fixed; /* Stay in place */
  top: 0;
  right: 0;
  left: 0;
  z-index: 9;
  overflow-x: hidden;
  overflow-y: auto;
  display: grid;
  grid-template-rows: auto;
  grid-template-columns: repeat(12, 1fr);
}
.modal-backdrop {
  position: fixed;
  width: 100%;
  height: 100%;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.3);
  z-index: 1;
}
.modal-dialog {
  position: relative;
  z-index: 2;
  grid-column: 5 / 9;
  grid-row: 1;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
  margin-top: 100px;
  background-color: #577a97;
  border-radius: 10px;
}
.modal-header {
  grid-column: 1 / 13;
  grid-row: 1;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
}
.modal-close {
    cursor: pointer;
    margin: 0 3px 0 10px;
    font-size: 1.5vw;
    grid-column: 12;
}
.modal-body {
  grid-column: 1 / 13;
  grid-row: 2;
}
</style>