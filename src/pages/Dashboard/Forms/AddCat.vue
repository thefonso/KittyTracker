<template>
  <div v-if="profilePic">
    <second-step v-show="profilePic"></second-step>
  </div>
  <div v-else>

    <form id="cat_form" @submit.prevent="validateBeforeSubmit">
      <!--alerts BEGINS-->
      <div class="row">
        <div class=""></div>

        <b-alert class="col-12" variant="success" dismissible fade :show="showSuccess">
          <strong>Success!</strong> New kitty added.
        </b-alert>

        <b-alert class="col-12" variant="danger" dismissible fade :show="showDanger">
          <strong>Problem:</strong> Did you fill out all fields? Are you connected to the internet?
        </b-alert>

        <div class=""></div>
      </div>
      <!--alerts ENDS-->
      <div class="container-fluid">
        <div class="row">
          <!--<div class="divTableHead col-sm-2 center">Photo</div>-->
          <div class="divTableCell col center">
            <div>
              <fg-input label="name" id="name"
                        onfocus="this.value=''"
                        name="name" placeholder="Name"
                        v-model="name" v-validate="'required'"
                        class="name" type="text">
              </fg-input>
            </div>
            <small v-show="errors.has('name')"
                   class="help is-danger form-text">{{ errors.first('name') }}
            </small>
          </div>
          <div class="divTableCell col center">
            <label>Gender</label>
            <div>
              <el-select class="select-secondary"
                      id="gender" name="gender"
                      v-model="select_gender.simple"
                      v-validate="'required'"
                      placeholder="Gender">
                <el-option v-for="option in select_gender.gender"
                           class="select-secondary"
                           :value="option.value"
                           :label="option.label"
                           :key="option.label">
                </el-option>
              </el-select>
            </div>
            <small class="help is-danger" v-show="errors.has('gender')">{{ errors.first('gender') }}</small>
          </div>
          <!--TODO: DATE PICKER SIZE-->
          <div class="divTableCell col-sm-3 center birthday">
            <div>
              <label>BirthDate</label>
              <fg-input>
                <el-date-picker v-model="birthday" v-validate="'required|date_format:YYYY-MM-DD'" type="date"
                                placeholder="yyyy-mm-dd" format="yyyy/MM/dd" value-format="yyyy-MM-dd"
                                :picker-options="pickerOptions1">
                </el-date-picker>
                <small v-show="errors.has('birthday')" class="help is-danger form-text">{{ errors.first('birthday') }}</small>
              </fg-input>
            </div>
          </div>
          <div class="divTableCell col center">
            <label>Type</label>
            <div>
              <el-select class="select-secondary"
                         id="catType" name="catType"
                         v-model="selects.simple"
                         v-validate="'required'">
                <el-option v-for="option in selects.catType"
                           class="select-secondary"
                           :value="option.value"
                           :label="option.label"
                           :key="option.label">
                </el-option>
              </el-select>
            </div>
            <small class="help is-danger form-text" v-show="errors.has('catType')">{{ errors.first('catType') }}</small>
          </div>
          <div class="divTableCell col center">
            <div v-if="catType === 'P' || catType === 'NM' || catType === 'NK'" >
              <label>Create Litter?</label>
              <div>
                <div class="form-check-inline">
                  <input class="form-check-input" type="radio" name="AddKittens" id="AddKittens1" value="Y"
                         @click="showModal">
                  <label class="form-check-label" for="AddKittens1">Yes</label>
                </div>
                <div class="form-check-inline">
                  <input class="form-check-input" type="radio" name="AddKittens" id="AddKittens2" value="N">
                  <label class="form-check-label" for="AddKittens2">No</label>
                </div>
              </div>
            </div>
            <div v-else-if="catType !== 'P' || catType !=='NM' || catType !=='NK'">
              <label>Litter</label>
              <div>
                <el-select class="select-secondary"
                           name="litter_set"
                           v-model="litter">
                  <el-option selected value="none">none</el-option>
                  <el-option v-for="item in litter" :value="item.name" :key="item.id">{{item.name}}</el-option>
                </el-select>
              </div>
            </div>
          </div>
          <div class="divTableCell col center">
            <div>
              <fg-input label="weight" id="weight"
                        onfocus="this.value=''"
                        name="weight" placeholder="Weight"
                        v-model="weight" v-validate="'required|integer'"
                        class="weight" type="text"/>
            </div>
            <small v-show="errors.has('weight')" class="help is-danger form-text">{{ errors.first('weight') }}</small>
          </div>
          <div class="divTableCell col center">
            <label>Unit</label>
            <div>
              <el-select class="select-secondary"
                         name="weight_unit"
                         v-model="select_unit.simple"
                         v-validate="'required|alpha'">
                <el-option v-for="option in select_unit.weight_unit"
                           class="select-secondary"
                           :value="option.value"
                           :label="option.label"
                           :key="option.label">
                </el-option>
              </el-select>
              <small v-show="errors.has('weight_unit')" class="help is-danger form-text">{{ errors.first('weight_unit') }}</small>
            </div>
          </div>
          <!--TODO: fill out new kitten litter form here-->
          <!-- Modal Component -->
          <b-modal id="kitten_modal" centered size="lg" class="pt-sm-5" ref="myModalRef" hide-footer title="Create A Litter">
            <b-container fluid>
              <p class="my-4"></p>
              <div class="row">
                <div class="col-2"></div>
                <b-alert class="col-8" variant="success" dismissible fade :show="showSuccess_litter">
                  <strong>Success!</strong> New litter added.
                </b-alert>

                <b-alert class="col-8" variant="danger" dismissible fade :show="showDanger_litter">
                  <strong>Problem:</strong> Did you fill out all fields? Are you on the internet?
                </b-alert>
                <div class="col-2"></div>
              </div>
              <form id="kitten-form" @submit.prevent="validateBeforeSubmitLitter">
                <div id="kitten-content" class="form-group row">
                  <div class="col-2"></div>

                  <!--second column-->
                  <div class="col-4 float-left">
                    <div class="form-group">
                      <label class="col-12" for="lit_name">New Litter's Name</label>
                      <div class="col-12">
                        <input id="lit_name"
                               name="litter_name"
                               v-model="litter_name"
                               :class="{'input': true, 'is-danger': errors.has('litter_name'),}"
                               class="form-control"
                               type="text">
                        <small v-show="errors.has('litter_name')" class="help is-danger form-text">{{ errors.first('litter_name') }}</small>
                      </div>
                    </div>
                    <!--NOTE: litter stuff ends here-->
                  </div>
                  <!--third column-->
                  <div class="col-4 float-left">
                    <div class="form-group">
                      <label class="col-12">Mama cats name</label>
                      <div class="col-8">
                        <input name="birthday"
                               onfocus="this.value=''"
                               v-model="name"
                               v-validate="'required'"
                               :class="{'input': true, 'is-danger': errors.has('name') }"
                               class="form-control"
                               type="text">
                        <small v-show="errors.has('name')" class="help is-danger form-text">{{ errors.first('name') }}</small>
                      </div>
                    </div>
                    <div class="clear-fix"></div>
                    <div class="form-group">
                      <div class="col-8">
                        <button :disabled="errors.any()" type="submit" name="kitten-button" value="button2" class="btn btn-primary submit-button">Submit</button>
                      </div>
                    </div>
                  </div>
                  <div class="col-1"></div>
                </div>
              </form>
            </b-container>
          </b-modal>
          <!--NOTE: litter stuff ends here-->
        </div>
      </div>
      <div class="col form-group container-fluid">
        <!--NOTE: someone decided to remove the key form field that all the complex logic was related to.-->
        <div v-if="catType === 'O' || catType === 'NK'">
          <input type="hidden" name="age" value="K" v-bind="age = 'K'" v-model="age" placeholder="K">
        </div>
        <div v-if="catType !== 'O' || catType !== 'NK'">
          <input type="hidden" name="age" value="A" v-bind="age = 'A'" v-model="age" placeholder="A">
        </div>
        <div class="d-flex justify-content-center row">
          <button :disabled="errors.any()"
                  type="submit"
                  name="cat-button"
                  value="button1"
                  class="btn btn-primary submit-button save-button rectangle-79 save">Save</button>
          <button type="reset"
                  name="cat-exit"
                  value="button2"
                  class="btn btn-primary submit-button exit-button rectangle-79 exit" @click="hideMe">Exit</button>
        </div>
      </div>
    </form>

  </div>
</template>

<script>
  import { DatePicker, TimeSelect, Slider, Tag, Input, Button, Select, Option } from 'element-ui'
  import axios from 'axios';
  import {Observable} from 'rxjs';
  import SecondStep from './Wizard/SecondStep.vue'
  import initialStateAddaCat from '../Tables/ExtendedTables';
  import showSwal from '../Tables/ExtendedTables';
  import {
    Progress as LProgress,
    Switch as LSwitch,
    Radio as LRadio,
    Checkbox as LCheckbox,
    FormGroupInput as FgInput
  } from '../../../components/index'


  export default {
    name: "AddCat",
    data () {
      return {
        catType: '',
        profilePic: false,
        name: '',
        select_gender: {
          simple:'',
          gender: [{value:'M',label:'Male'},{value:'F',label:'Female'}],
        },
        age: '',
        selects:{
          simple:'',
          catType: [{value:'O', label:'Orphan Kitten'},
            {value:'NK', label:'Nursing Kitten'},
            {value:'NM', label:'Nursing Mom'},
            {value:'P', label:'Pregnant Mom'},
            {value:'A', label:'Adult'},
          ],
        },
        select_unit: {
          simple:'',
          weight_unit: [{value:'G',label:'Grams'}, {value:'LB',label:'Pounds'}
          ],
        },
        litter: [],
        litter_mates: null,
        litter_name: '',
        pickerOptions1: {
          disabledDate(time) {
            return time.getTime() > Date.now();
          },
          shortcuts: [{
            text: 'Today',
            onClick (picker) {
              picker.$emit('pick', new Date())
            }
          },
            {
              text: 'Yesterday',
              onClick (picker) {
                const date = new Date()
                date.setTime(date.getTime() - 3600 * 1000 * 24)
                picker.$emit('pick', date)
              }
            },
            {
              text: 'A week ago',
              onClick (picker) {
                const date = new Date()
                date.setTime(date.getTime() - 3600 * 1000 * 24 * 7)
                picker.$emit('pick', date)
              }
            }]
        },
        datePicker: '',
        options: {
          format: 'YYYY-MM-DD',
          useCurrent: false,
        },
        mom_cat: '',
        female: false,
        addKittens: false,
        cat_form: true,
        selectedFile: null,
        singleCat: [],
        photo: '',
        showSuccess: false,
        showDanger: false,
        showSuccess_litter: false,
        showDanger_litter: false,
        weight: '',
        birthday: '',
      }
    },
    methods: {
      resetWindow (){
        this.$data = initialStateAddaCat();
      },
      onFileChanged (event) {
        this.selectedFile = event.target.files[0];
        this.onUpload();
      },
      onUpload() {
        // upload file, get it from this.selectedFile
        const formData = new FormData();
        formData.append('name', this.name);
        formData.append('photo', this.selectedFile, this.selectedFile.name);
        axios.put(`/api/v1/cats/${this.$route.params.catID}/`,formData,{
          onUploadProgress: progressEvent => {
            console.log('Upload progress: ' + Math.round(progressEvent.loaded / progressEvent.total * 100) + '%')
          }
        })
          .then(response => {
            console.log(response.data.photo);
            // response.status === 201 ? this.showSuccess = true : this.showDanger = true
            this.singleCat = response.data;
          })
          .catch(error => {
            console.log(error);
            // this.showDanger = true;
          })
      },
      onSubmitted() {
        axios.post(`/api/v1/cats/`, {
          name: this.name,
          age: this.age,
          gender: this.gender,
          catType: this.catType,
          litter: this.litter,
          weight: this.weight,
          birthday: this.birthday,
          weight_unit: this.weight_unit
        })
          .then(response => {
            console.log(response);
            response.status === 201 ? this.showSuccess = true : this.showDanger = true;
            this.profilePic = true;
          })
          .catch(error => {
            console.log(error);
            this.showDanger = true;
          })
      },
      validateBeforeSubmit() {
        this.$validator.validateAll()
          .then((result) => { console.log(result);
            this.onSubmitted();
          }).catch(error => {
          console.log(error);
          this.showDanger = true;
        });
      },
      onSubmittedLitter() {
        axios.post(`/api/v1/litter/`, {
          litter_name: this.litter_name,
          mom_cat: this.name,
        })
          .then(response => {
            console.log(response);
            response.status === 201 ? this.showSuccess_litter = true : this.showDanger_litter = true;
            this.cat_form = true;
          })
          .catch(error => {
            console.log(error);
            this.showDanger_litter = true;
          })
      },
      validateBeforeSubmitLitter() {
        this.$validator.validateAll().then((result) => {
          if (result) {
            this.onSubmittedLitter();
          } else {
            // this.showDanger = true;
          }
        });
      },
      getLitterNames() {
        axios.get(`/api/v1/litter/`)
          .then(request => {
            console.log("litter_value: ");
            this.litter = request.data.results;
            console.log(this.litter);
          })
          .catch(error => console.log(error));
      },
      getLitterNamesObserv() {
        const litter$ = Observable.from(axios.get(`/api/v1/litter/`)
          .catch(error => console.log(error)))
          .pluck("data", "results");
        console.log(litter$);
        return {litter: litter$}
      },
      showModal () {
        this.$refs.myModalRef.show();
        // TODO: turn validate off here
        this.cat_form = false;
      },
      hideModal () {
        this.$refs.myModalRef.hide();
      },
      hideMe () {
        document.getElementById("rectangle-255").click();
      },
      getError (fieldName) {
        return this.errors.first(fieldName)
      },
      validate () {
        return this.$validator.validateAll().then(res => {
          console.log("fuq");
          this.$emit('on-validated', res, this.model);
          return res
        })
      }
    },
    beforeMount() {
      this.getLitterNames()
    },
    components: {
      SecondStep,
      FgInput,
      [DatePicker.name]: DatePicker,
      [TimeSelect.name]: TimeSelect,
      [Slider.name]: Slider,
      [Tag.name]: Tag,
      [Input.name]: Input,
      [Button.name]: Button,
      [Option.name]: Option,
      [Select.name]: Select,
      LSwitch,
      LProgress,
      LRadio,
      LCheckbox
      // 'b-modal': bModal,
      // 'b-container': bContainer,
      // 'b-alert': bAlert
    },
    directives: {
      // 'b-modal': bModalDirective
    },
  }
</script>

<style scoped>
  /*add-a-cat menu begins*/
  .bg-copy-10 {
    height: 17px;
    width: 59px;
    border: 1px solid #E7E7E9;
    border-radius: 4px;
    background-color: #FFFFFF;
    font-family: Roboto;
    font-size: 11px;
    line-height: 17px;
    text-align: center;
  }
  .date_picker {
    height: 17px;
    width: 84px;
  }
  .save-button{
    margin-right: 5px;
  }
  .exit-button{
    margin-left: 5px;
  }
  .rectangle-79 {
    height: 29px;
    width: 106px;
    border: 1px solid #979797;
    border-radius: 4px;
    background-color: #23CCEF;
  }
  .save{
    height: 29px;
    width: 94px;
    color: #4A4A4A;
    font-family: Roboto;
    font-size: 14px;
    font-weight: bold;
    line-height: 20px;
    text-align: center;
  }
  .exit{
    height: 29px;
    width: 94px;
    color: #4A4A4A;
    font-family: Roboto;
    font-size: 14px;
    font-weight: bold;
    line-height: 20px;
    text-align: center;
  }
  .el-picker-panel .el-date-picker {
    height: 64px;
    width: 99px;
  }
  .name{
    width: 59px;
  }
  .gender{
    width: 59px;
  }
  .litter_name{
    width: 122px;
  }
  .weight{
    width: 64px;
  }
  .unit{
    width: 53px;
  }
  /*add-a-cat menu ends*/
</style>
