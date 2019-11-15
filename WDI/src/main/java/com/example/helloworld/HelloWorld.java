package com.example.helloworld;

import java.io.File;
import java.io.FileReader;

import au.com.bytecode.opencsv.CSVReader;
import de.uni_mannheim.informatik.dws.winter.matching.MatchingEngine;
import de.uni_mannheim.informatik.dws.winter.model.Correspondence;
import de.uni_mannheim.informatik.dws.winter.model.DataSet;
import de.uni_mannheim.informatik.dws.winter.model.HashedDataSet;
import de.uni_mannheim.informatik.dws.winter.model.defaultmodel.Attribute;
import de.uni_mannheim.informatik.dws.winter.model.defaultmodel.CSVRecordReader;
import de.uni_mannheim.informatik.dws.winter.model.defaultmodel.Record;
import de.uni_mannheim.informatik.dws.winter.model.defaultmodel.comparators.LabelComparatorJaccard;
import de.uni_mannheim.informatik.dws.winter.model.defaultmodel.comparators.LabelComparatorLevenshtein;
import de.uni_mannheim.informatik.dws.winter.processing.Processable;
import de.uni_mannheim.informatik.dws.winter.utils.WinterLogManager;
import org.slf4j.Logger;

import org.json.JSONObject;
import org.json.JSONString;
//import org.json.simple.JSONArray;
//import org.json.simple.parser.ParseException;
//import org.json.simple.parser.JSONParser;

import java.util.Iterator;
import java.io.FileWriter;
import java.io.BufferedWriter;

public class HelloWorld {

//    private static final Logger logger = WinterLogManager.activateLogger("default");

    public static void main(String[] args) throws Exception {

        CSVReader reader = new CSVReader(new FileReader("offers.csv"));
        reader.readNext(); // read the header and ignore it
        String[] line; // store one line of offer

        // process each offer iteratively
        while ((line = reader.readNext()) != null) {

            //--------------------- create a csv out of each offer -----------------------
            String node_id = line[4];
            String url = line[3];
            String kvp = line[6];
            JSONObject kvpJson = new JSONObject(kvp);
            Iterator iter = kvpJson.keys();
            String keys = "";
            while (iter.hasNext()) {
                if (keys.length() == 0) {
                    keys = iter.next().toString();
                } else {
                    keys = keys + "," + iter.next();
                }
            }
            FileWriter writer = new FileWriter("./offer.csv");
            writer.append(node_id + "," + url + "," + keys);
            writer.close();
            //---------------------------------------------------------------------------

            // load data
            DataSet<Record, Attribute> data1 = new HashedDataSet<Record, Attribute>();
            new CSVRecordReader(0).loadFromCSV(new File("keys_dict.csv"), data1);
            DataSet<Record, Attribute> data2 = new HashedDataSet<Record, Attribute>();
            new CSVRecordReader(0).loadFromCSV(new File("offer.csv"), data2);

            // Initialize Matching Engine
            MatchingEngine engine = new MatchingEngine<Attribute, Attribute>();

            Processable<Correspondence<Attribute, Attribute>> correspondences = engine.runLabelBasedSchemaMatching(data1.getSchema(), data2.getSchema(), new LabelComparatorJaccard(), 0.5);

            // print results
            for (Correspondence<Attribute, Attribute> cor : correspondences.get()) {
//            logger.info(String.format("[%s]'%s' <-> [%s]'%s' (%.4f)",
//                    cor.getFirstRecord().getIdentifier(),
//                    cor.getFirstRecord().getName(),
//                    cor.getSecondRecord().getIdentifier(),
//                    cor.getSecondRecord().getName(),
//                    cor.getSimilarityScore()));
                File file = new File("./goldstandard.csv");
                FileWriter writer2 = new FileWriter(file, true);
                BufferedWriter br = new BufferedWriter(writer2);
                br.write(node_id + "," + url + "," + String.format("'%s','%s'", cor.getFirstRecord().getName(), cor.getSecondRecord().getName()) + "\n");
                br.close();
                writer2.close();
//                writer2.append(node_id + "," + url + "," + String.format("'%s','%s'", cor.getFirstRecord().getName(), cor.getSecondRecord().getName()));
//                writer2.close();

                //System.out.println(node_id + "," + url + "," + String.format("'%s','%s'", cor.getFirstRecord().getName(), cor.getSecondRecord().getName()));
            }

//        // Initialize Matching Engine
//        MatchingEngine engine = new MatchingEngine<Record, Attribute>();
//
//        Processable<Correspondence<Attribute, Record>> correspondences = engine.runLabelBasedSchemaMatching(data1.getSchema(), data2.getSchema(), new LabelComparatorLevenshtein(), 0.4);
//
//        // print results
//        for(Correspondence<Attribute, Record> cor : correspondences.get()) {
//            logger.info(String.format("[%s]'%s' <-> [%s]'%s' (%.4f)",
//                    cor.getFirstRecord().getIdentifier(),
//                    cor.getFirstRecord().getName(),
//                    cor.getSecondRecord().getIdentifier(),
//                    cor.getSecondRecord().getName(),
//                    cor.getSimilarityScore()));
//        }

            // delete file
//            File file = new File("./offer.csv");
//            file.delete();
        }
    }
}
