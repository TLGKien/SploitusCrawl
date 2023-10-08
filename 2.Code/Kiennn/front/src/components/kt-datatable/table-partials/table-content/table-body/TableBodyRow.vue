<template>
  <tbody class="fw-semibold text-gray-600">
    <template v-for="(row, i) in data" :key="i">
      <tr>
        <td v-if="checkboxEnabled">
          <div
            class="form-check form-check-sm form-check-custom form-check-solid"
          >
            <input
              class="form-check-input"
              type="checkbox"
              :value="row[checkboxLabel]"
              v-model="selectedItems"
              @change="onChange"
            />
          </div>
        </td>

        <td class="hidden-column text-dark fw-bold fs-6}">
          <slot :name="`pk`" :row="row">
            {{ row.pk }}
          </slot>
        </td>

        <td>
          <slot :name="`projectName`" :row="row">
            <a
              href="#"
              class="text-dark fw-bold text-hover-primary d-block mb-1 fs-6"
              data-bs-toggle="modal"
              data-bs-target="#kt_modal_add_customer"
              >{{ row.projectName }}</a
            >
            <span class="text-muted fw-semobold text-muted d-block fs-7"
              >{{ row.projectDescription }}</span
            >
          </slot>
        </td>

        <td>
          <slot :name="`partner`" :row="row">
            <a
              href="#"
              class="text-dark fw-bold text-hover-primary fs-6"
              >{{ row.partner }}</a
            >
          </slot>
        </td>

        <td>
          <slot :name="`manager`" :row="row">
            <a
              href="#"
              class="text-dark fw-bold text-hover-primary fs-6"
              >{{ row.manager }}</a
            >
          </slot>
        </td>

        <td class="text-dark fw-bold fs-6">
          <slot :name="`startDate`" :row="row">
            {{ row.startDate }}
          </slot>
        </td>

        <td class="text-dark fw-bold fs-6">
          <slot :name="`dueDate`" :row="row">
            {{ row.dueDate }}
          </slot>
        </td>
        <td class="text-dark fw-bold fs-6">
          <slot :name="`budget`" :row="row">
            {{ row.budget }}
          </slot>
        </td>
        
        <td>
          <slot :name="`status`" :row="row">
            <span
              :class="`badge-light-${row.status}`"
              class="badge"
              >{{ row.status }}
            </span>
          </slot>
        </td>

        <td class="text-end">
          <slot :name="`actions`" :row="row">
            <a
              href="#"
              class="btn btn-icon btn-bg-light btn-active-color-primary btn-sm me-1"
              data-bs-toggle="modal"
              data-bs-target="#kt_modal_edit_project"
            >
              <KTIcon icon-name="pencil" icon-class="fs-3" />
            </a>
            

            <a
              href="#"
              class="btn btn-icon btn-bg-light btn-active-color-primary btn-sm"
              data-bs-toggle="modal"
              data-bs-target="#kt_modal_delete_project"
            >
              <KTIcon icon-name="trash" icon-class="fs-3" />
            </a>
            
          </slot>
        </td>

      </tr>
      <EditProjectModal :pk="row.pk"/>
      <DeleteProjectModal/>
    </template>
    
  </tbody>

</template>

<script lang="ts">
import { defineComponent, ref, watch } from "vue";
import EditProjectModal from "@/components/modals/forms/EditProjectModal.vue";
import DeleteProjectModal from "@/components/modals/forms/DeleteProjectModal.vue";

export default defineComponent({
  name: "table-body-row",
  components: {
    EditProjectModal,
    DeleteProjectModal,
  },
  props: {
    header: { type: Array as () => Array<any>, required: true },
    data: { type: Array as () => Array<any>, required: true },
    currentlySelectedItems: { type: Array, required: false, default: () => [] },
    checkboxEnabled: { type: Boolean, required: false, default: false },
    checkboxLabel: {
      type: String as () => string,
      required: false,
      default: "id",
    },
  },
  emits: ["on-select"],
  setup(props, { emit }) {
    const selectedItems = ref<Array<any>>([]);

    watch(
      () => [...props.currentlySelectedItems],
      (currentValue) => {
        if (props.currentlySelectedItems.length !== 0) {
          selectedItems.value = [
            ...new Set([...selectedItems.value, ...currentValue]),
          ];
        } else {
          selectedItems.value = [];
        }
      }
    );

    const onChange = () => {
      emit("on-select", selectedItems.value);
    };

    return {
      selectedItems,
      onChange,
    };
  },
});
</script>
<style scoped>
  .hidden-column {
    display: none;
  }
</style>