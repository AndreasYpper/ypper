<template>
  <div class="create-status-container">
    <div class="create-status-form-container">
      <div class="header">
        <h1>Cereate Machine Status</h1>
      </div>
      <form class="create-status-form" @submit.prevent="createStatus">
        <label class="form-label">Title: </label>
        <input
          class="form-field"
          v-model="form.title"
          type="text"
          placeholder="Title"
        />
        <div class="error" v-if="error.title!=''">
          <p>{{ error.title }}</p>
        </div>
        <div class="button-group">
          <button class="create-button">Create</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { reactive, getCurrentInstance } from "vue";
import axios from "axios";
export default {
  setup() {
    const instance = getCurrentInstance();
    const form = reactive({
      title: "",
    });

    const error = reactive({
      title: "",
    });

    function validateForm() {
      if (form.title.length > 0) {
        return true;
      } else {
        error.title = "Title field can't be left blank.";
        return false;
      }
    }

    function createStatus() {
      if (validateForm()) {
        axios
          .post(process.env.VUE_APP_API_URL + "machine_statuses", form)
          .then((response) => {
            if (response.data.title == form.title) {
              instance.parent.setupState.create_status = false;
            }
          });
      }
    }

    return {
      form,
      error,
      validateForm,
      createStatus,
    };
  },
};
</script>

<style scoped>
.create-status-container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
}
.create-status-form-container {
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
.create-status-form {
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
  /* color: #a9a9a9; */
  color: black;
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
.error {
  grid-column: 2 / 12;
  color: #ff3b3f;
  font-style: italic;
  font-size: 1vw;
}
</style>