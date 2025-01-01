import { promises as fs } from 'fs';
import { decode } from 'base65537';
import open from 'open';

try {
    const data_from_file = await fs.readFile('../files/congrats.txt', 'utf-8');
    // console.log(data_from_file);

    const data_from_base65537 = Buffer.from(
        decode(data_from_file) // decoding from base65537
    ).toString('utf-8');
    // console.log(data_from_base65537);

    const data_from_base64 = Buffer.from(data_from_base65537, 'base64');
    // console.log(data_from_base64);

    const output_file = './output.png';
    await fs.writeFile(output_file, data_from_base64);
    console.log(`Image enregistrée avec succès dans : ${output_file}`);

    await open(output_file);
    console.log('Image affichée à l’écran.');
} catch (error) {
    console.error('Erreur lors de la lecture du fichier :', error);
}