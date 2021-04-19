<template>
  <div class="create-machine-container">
    <div class="create-machine-form-container">
      <div class="header">
        <h1>Create Machine</h1>
      </div>
      <form class="create-machine-form" @submit.prevent="createMachine">
        <label class="form-label"> Name: </label>
        <input
          class="form-field"
          v-model="form.name"
          type="text"
          placeholder="Name"
        />
        <div class="error" v-if="error.name!=''">
          <p>{{ error.name }}</p>
        </div>
        <!-- <label class="form-label"> Warrenty of lasertube expires: </label>
        <input
          class="form-field"
          type="text"
          placeholder="Warrenty of lasertube expires"
          onfocus="(this.type='date')"
        /> -->
        <div class="button-group">
          <button class="create-button">Create</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { reactive, getCurrentInstance } from "vue";
import axios from 'axios'
export default {
  setup() {
    const instance = getCurrentInstance()
    const form = reactive({
      name: "",
    });

    const error = reactive({
      name: "",
    });

    function validateForm() {
      if(form.name.length > 0) {
        return true
      }
      else{
        error.name = "Name field can't be left blank."
        return false
      }
    }

    function createMachine() {
      if (validateForm()) {
        axios.post(process.env.VUE_APP_API_URL + 'machine', form)
          .then((response) => {
            if(response.data.name == form.name) {
              instance.parent.setupState.create_modal = false
            }
          })
      }
    }

    return {
      form,
      error,
      validateForm,
      createMachine,
    };
  },
};
</script>

<style scoped>
.create-machine-container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
}
.create-machine-form-container {
  grid-column: 1 / 13;
  grid-row: 1;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
  background-color: #fefefe;
  border-radius: 10px;
}
.header {
  grid-row: 1;
  grid-column: 2 / 12;
  color: #a9a9a9;
}
.create-machine-form {
  grid-column: 2 / 12;
  grid-row: 2;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
}
.form-field {
  grid-column: 1 / 13;
  margin: 10px;
  height: 2vw;
  border-radius: 10px;
  border: none;
  text-align: center;
  font-family: "Ubuntu", sans-serif;
  font-size: 1vw;
  background-color: #caebf2;
}
.form-field:focus {
  outline: none;
  border: 2px solid #caebf2;
}
.form-field::placeholder {
  font-family: "Ubuntu", sans-serif;
  font-size: 1vw;
  color: caebf2;
}
.form-label {
  grid-column: 1 / 13;
  text-align: left;
  margin: 10px;
  color: #a9a9a9;
}
.button-group {
  grid-column: 2 / 12;
  margin: 10px;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
}
.create-button {
  grid-column: 4 / 10;
  height: 2.5vw;
  font-family: "Ubuntu", sans-serif;
  font-size: 1vw;
  border-radius: 10px;
  border: none;
  background-color: #1ffaa6;
  cursor: pointer;
}
.error{
  grid-column: 2 / 12;
  color: #ff3b3f;
  font-style: italic;
  font-size: 1vw;
}
</style>