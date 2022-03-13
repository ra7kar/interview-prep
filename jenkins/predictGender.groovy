import groovy.json.JsonSlurper

properties([
    parameters([
        string(name: 'name', defaultValue: 'Sam')
    ])
])

def predictGender(String name) {
        def get = new URL("https://api.genderize.io/?name=${name}").openConnection();
    def getRC = get.getResponseCode();
    if (getRC.equals(200)) {
        def slurper = new groovy.json.JsonSlurper();
        def result = slurper.parseText(get.getInputStream().getText());
        return [result.gender, result.count];
    } else {
        throw new Exception("HTTP Request to api.genderize.io failed");
    }
}

node {
    gender, count = predictGender(params.name)
    stage('Predict Gender') { 
        echo "Predicting Gender for: ${params.name}"
        echo "Probability of prediction: ${gender}"
        echo "Count: ${count}"
    }
}
