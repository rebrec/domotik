JSONEditor.defaults.options.theme = 'bootstrap3';
JSONEditor.defaults.iconlib = 'bootstrap3';
JSONEditor.defaults.options.object_layout = "grid";


$().ready(function() {
    $('#editor').hide();
    $('#editor').val(JSON.stringify(jsonConfig, null, '\t'));
    $('#debug').click(function(event){  $('#editor').toggle();});

    $('#annuler').click(function(e) {
        location.reload(true);
    });

    $("form#restart").on("submit", function(event) {
        event.preventDefault();
        console.log($(this).serialize());

        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: $(this).serialize(), // I WANT TO ADD EXTRA DATA + SERIALIZE DATA
            success: function(data) {
                console.log(data);
                if (data['result'] == 'done') {
                    alert("Redemarrage en cours, pensez a actualiser la page et a changer éventuellement de port !");
                } else {
                    alert("Erreur !");
                }
            }
        });
    });

    $("form#save").on("submit", function(event) {
        $('#editor').val(JSON.stringify(editor.getValue(), null, "\t"));
        event.preventDefault();
        console.log($(this).serialize());

        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: $(this).serialize(), // I WANT TO ADD EXTRA DATA + SERIALIZE DATA
            success: function(data) {
                console.log(data);
                if (data['result'] == 'done') {
                    alert("Sauvegardé!");
                } else {
                    alert("Erreur Structure Incorrecte !");
                }
            }
        });
    });


    var editor = new JSONEditor(document.getElementById('editor_holder'), {
        // Enable fetching schemas via ajax
        ajax: true,
        startval: jsonConfig,

        // The schema for the editor
        schema: {
            "type": "object",
            "id":"z",
            "properties": {
                "listen": {
                    "type": "integer",
                    "title": "Port d'Ecoute",
                    "minimum": 1,
                    "maximum": 65535,
                    "default":"80"

                },
                "interrupteurs": {
                    "type": "array",
                    "title": "Interrupteurs",
                    "uniqueItems": true,
                    "format": "tabs",
                    "items": {

                        "headerTemplate": "{{i}} - {{self.param.name}}",
                        oneOf: [{
                            $ref: "/static/js/interrupteur_sf.json",
                            title: "Interrupteur S/F"
                        }, {
                            $ref: "/static/js/minuterie.json",
                            title: "Minutterie"
                        }]
                    }

                }

            }
        },

        // Seed the form with a starting value
        //startval: starting_value,

        // Disable additional properties
        no_additional_properties: true,
        disable_collapse: true,
        disable_edit_json: true,
        disable_properties: true,

        // Require all properties by default
        required_by_default: true
    });

    document.getElementById('show_code').addEventListener('click',function() { console.log(JSON.stringify(editor.getValue(), null, "\t")); });
});