var app = new Vue({
    el: '#feature_settings',
    delimiters: ['[[', ']]'],
    data() {
        return {
            features: [],
            setFeature: 2,
        }
    },
    mounted(){
        document.getElementById('id_extrafeature_set-TOTAL_FORMS').getAttribute('value')
        this.setFeature = document.getElementById('id_extrafeature_set-TOTAL_FORMS').getAttribute('value')
    },
    methods: {
        addFeature() {
            const schema = {
                idExtra: `id_extrafeature_set-${this.setFeature}-feature`,
                labelName: 'Feature name:',
                extraFeature: `extrafeature_set-${this.setFeature}-feature`,
                idExtraChoice: `id_extrafeature_set-${this.setFeature}-choice`,
                labelNameChoice: 'Choice:',
                extraFeatureChoice: `extrafeature_set-${this.setFeature}-choice`,
                extraFeatureSetChoiceId: `id_extrafeature_set-${this.setFeature}-id`,
                extraFeatureSetId: `extrafeature_set-${this.setFeature}-id`,
                extraFeatureSetIdProperty: `id_extrafeature_set-${this.setFeature}-property`,
                extraFeatureProperty: `extrafeature_set-${this.setFeature}-property`

            }
            console.log(document.getElementById('id_extrafeature_set-TOTAL_FORMS').getAttribute('value'))
            this.setFeature += 1
            this.features.push(schema)
            document.getElementById('id_extrafeature_set-TOTAL_FORMS').setAttribute('value', this
                .setFeature)
        }
    }


})