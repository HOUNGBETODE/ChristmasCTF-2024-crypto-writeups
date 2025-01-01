const rot47 = require('@sefinek/rot47');
const fs = require('fs');


(async () => {
  try {
    const inputPath = '../files/download.jpg';
    const outputPath = './original.jpg';

    // Lecture du contenu de 'download.jpg'
    const imageBuffer = fs.readFileSync(inputPath);
    console.log('Image originale chargée avec succès.');

    // Transformation du contenu de 'download.jpg'
    const originalBuffer = Buffer.from(
        rot47.decode(
            imageBuffer.toString('binary')
        ), 
        'binary'
    );

    // Sauvegarde du nouveu contenu dans 'original.jpg'
    fs.writeFileSync(outputPath, originalBuffer);
    console.log(`Image modifiée sauvegardée avec succès : ${outputPath}`);
  } catch (error) {
    console.error('Erreur lors du traitement de l’image :', error);
  }
})();
