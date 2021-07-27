<template>
  <div class="create-post-container">
    <form class="create-post-form" @submit.prevent="createMachine">
      <labe class="form-label">Title: </labe>
      <input
        class="form-field"
        v-model="form.title"
        type="text"
        placeholder="Title"
      />
      <labe class="form-label">Content: </labe>
      <textarea
        class="form-field-textarea"
        v-model="form.content"
        rows="3"
        cols="20"
        placeholder="Add a description of the problem."
      >
      </textarea>
      <labe class="form-label">Author: </labe>
      <input
        class="form-field"
        v-model="form.author"
        type="text"
        placeholder="Who is that?"
      />
      <div class="button-group">
        <button class="create-button">Post</button>
        <button class="cancel-button" @click="toggleCreateForm()">Cancel</button>
      </div>
    </form>
  </div>
</template>

<script>
import stateMachine from '@/modules/machine'
import { reactive } from "vue";
export default {
  setup() {
    const { toggleShowCreatePost } = stateMachine
    const form = reactive({
      title: "",
      content: "",
      author: "",
    });

    function toggleCreateForm() {
      toggleShowCreatePost()
    }

    return {
      toggleCreateForm,
      form,
    };
  },
};
</script>

<style scoped>
.create-post-container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
}
.create-post-form {
  grid-column: 2 / 12;
  grid-row: 2;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
}
.form-field {
  grid-column: 1 / 13;
  margin: 5px;
  height: 1.5vw;
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
  font-size: 0.8vw;
  color: #516266;
}
.form-field-textarea {
  grid-column: 1 / 13;
  margin: 5px;
  border-radius: 10px;
  border: none;
  text-align: left;
  font-family: "Ubuntu", sans-serif;
  font-size: 0.8vw;
  background-color: #caebf2;
}
.form-field-textarea:focus {
  outline: none;
  border: 2px solid #caebf2;
}
.form-field-textarea::placeholder {
  font-family: "Ubuntu", sans-serif;
  font-size: 0.8vw;
  color: #516266;
}
.form-label {
  grid-column: 1 / 13;
  text-align: left;
  margin: 5px;
  /* color: #a9a9a9; */
  color: black;
}
.button-group {
  grid-column: 2 / 12;
  margin: 5px;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
}
.create-button {
  grid-column: 2 / 6;
  height: 2vw;
  font-family: "Ubuntu", sans-serif;
  font-size: 0.8vw;
  border-radius: 10px;
  border: none;
  background-color: #1ffaa6;
  cursor: pointer;
}
.cancel-button {
  grid-column: 8 / 12;
  height: 2vw;
  font-family: "Ubuntu", sans-serif;
  font-size: 0.8vw;
  border-radius: 10px;
  border: none;
  background-color: #ff3b3f;
  cursor: pointer;
}
.error {
  grid-column: 2 / 12;
  color: #ff3b3f;
  font-style: italic;
  font-size: 1vw;
}
</style>