$().ready(function(){



    setInterval(function update_data(){
        $.get(
            'inter/get/?all=1', // Le fichier cible côté serveur.
            'false', // Nous utilisons false, pour dire que nous n'envoyons pas de données.
            function (data){
                console.log(data);
                $.each(data, function(name, state){
                    if (state == true){
                        $('.' + name + ':contains("ON")').addClass('active');
                        $('.' + name + ':contains("ON")').addClass('btn-primary');
                        $('.' + name + ':contains("ON")').removeClass('default');
                        $('.' + name + ':contains("OFF")').removeClass('active');
                        $('.' + name + ':contains("OFF")').removeClass('btn-primary');
                        $('.' + name + ':contains("OFF")').addClass('default');

                    } else {
                        $('.' + name + ':contains("OF")').addClass('active');
                        $('.' + name + ':contains("OF")').addClass('btn-primary');
                        $('.' + name + ':contains("OF")').removeClass('default');
                        $('.' + name + ':contains("ON")').removeClass('active');
                        $('.' + name + ':contains("ON")').removeClass('btn-primary');
                        $('.' + name + ':contains("ON")').addClass('default');
                    }

                });
                /*
                */
            },
            'json' // Format des données reçues.
        );

    },2000);

/***************************************************************************/

});
