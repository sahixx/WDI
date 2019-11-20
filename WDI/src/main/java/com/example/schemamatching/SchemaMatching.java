package com.example.schemamatching;

import java.io.File;
import java.io.FileReader;

import au.com.bytecode.opencsv.CSVReader;
import de.uni_mannheim.informatik.dws.winter.matching.MatchingEngine;
import de.uni_mannheim.informatik.dws.winter.matching.aggregators.VotingAggregator;
import de.uni_mannheim.informatik.dws.winter.matching.blockers.InstanceBasedSchemaBlocker;
import de.uni_mannheim.informatik.dws.winter.model.Correspondence;
import de.uni_mannheim.informatik.dws.winter.model.DataSet;
import de.uni_mannheim.informatik.dws.winter.model.HashedDataSet;
import de.uni_mannheim.informatik.dws.winter.model.MatchableValue;
import de.uni_mannheim.informatik.dws.winter.model.defaultmodel.Attribute;
import de.uni_mannheim.informatik.dws.winter.model.defaultmodel.CSVRecordReader;
import de.uni_mannheim.informatik.dws.winter.model.defaultmodel.Record;
import de.uni_mannheim.informatik.dws.winter.model.defaultmodel.comparators.LabelComparatorJaccard;
import de.uni_mannheim.informatik.dws.winter.processing.Processable;

import de.uni_mannheim.informatik.dws.winter.matching.blockers.BlockingKeyIndexer.VectorCreationMethod;
import de.uni_mannheim.informatik.dws.winter.model.Correspondence;
import de.uni_mannheim.informatik.dws.winter.model.DataSet;
import de.uni_mannheim.informatik.dws.winter.model.HashedDataSet;
import de.uni_mannheim.informatik.dws.winter.model.Matchable;
import de.uni_mannheim.informatik.dws.winter.model.MatchableValue;
import de.uni_mannheim.informatik.dws.winter.model.defaultmodel.Attribute;
import de.uni_mannheim.informatik.dws.winter.model.defaultmodel.CSVRecordReader;
import de.uni_mannheim.informatik.dws.winter.model.defaultmodel.Record;
import de.uni_mannheim.informatik.dws.winter.model.defaultmodel.blocking.DefaultAttributeValuesAsBlockingKeyGenerator;
import de.uni_mannheim.informatik.dws.winter.processing.Processable;
import de.uni_mannheim.informatik.dws.winter.similarity.vectorspace.VectorSpaceMaximumOfContainmentSimilarity;
import de.uni_mannheim.informatik.dws.winter.similarity.vectorspace.VectorSpaceCosineSimilarity;
import de.uni_mannheim.informatik.dws.winter.utils.WinterLogManager;

import org.json.JSONObject;
//import org.json.simple.JSONArray;
//import org.json.simple.parser.ParseException;
//import org.json.simple.parser.JSONParser;

import java.util.Iterator;
import java.io.FileWriter;
import java.io.BufferedWriter;

public class SchemaMatching {

//    private static final Logger logger = WinterLogManager.activateLogger("default");

    public static void main(String[] args) throws Exception {
        //labelBased();
        instanceBased();
    }

    public static void instanceBased() throws Exception {
//        CSVReader reader_dict = new CSVReader(new FileReader("dict.csv"));
//        reader_dict.readNext(); // read the header and ignore it
//        String[] line; // store one line of offer
//
//        // process each offer iteratively
//        while ((line = reader_dict.readNext()) != null) {
//
//
//        }
//
//        CSVReader reader = new CSVReader(new FileReader("gs_offers_kvp.csv"));
//        reader.readNext(); // read the header and ignore it
//        //String[] line; // store one line of offer
//
//        // process each offer iteratively
//        while ((line = reader.readNext()) != null) {
//
//            //--------------------- create a csv out of each offer -----------------------
//            String node_id = line[1];
//            String url = line[0];
//            String kvp = line[2];
//            if (kvp.length() == 0) {
//                continue;
//            }
//            JSONObject kvpJson = new JSONObject(kvp);
//            Iterator iter = kvpJson.keys();
//            String keys = "";
//            String values = "";
//            while (iter.hasNext()) {
//                String key = iter.next().toString();
//                if (keys.length() == 0) {
//                    keys = key;
//                    values = kvpJson.getString(key);
//                } else {
//                    keys = keys + "," + key;
//                    values = values + "," + kvpJson.getString(key);
//                }
//            }
//
//            FileWriter writer = new FileWriter("./offer_instance.csv");
//            writer.append(node_id + '\n' + url + '\n');
//            writer.append(keys + '\n');
//            writer.append(values + '\n');
//            writer.close();
//            //---------------------------------------------------------------------------
//        }

        // load data
        DataSet<Record, Attribute> data1 = new HashedDataSet<Record, Attribute>();
        new CSVRecordReader(0).loadFromCSV(new File("test1.csv"), data1);
        DataSet<Record, Attribute> data2 = new HashedDataSet<Record, Attribute>();
        new CSVRecordReader(0).loadFromCSV(new File("test2.csv"), data2);

        // Initialize Matching Engine
        MatchingEngine<Record, Attribute> engine = new MatchingEngine<Record, Attribute>();

        // run the matching
        Processable<Correspondence<Attribute, MatchableValue>> correspondences
                = engine.runInstanceBasedSchemaMatching(
                data1,
                data2,
                new DefaultAttributeValuesAsBlockingKeyGenerator(data1.getSchema()),
                new DefaultAttributeValuesAsBlockingKeyGenerator(data2.getSchema()),
                VectorCreationMethod.TermFrequencies,
                new VectorSpaceCosineSimilarity(),
                0.0);






        // print results
        for(Correspondence<Attribute, MatchableValue> cor : correspondences.get()) {
            System.out.println(String.format("'%s' <-> '%s' (%.4f)", cor.getFirstRecord().getName(), cor.getSecondRecord().getName(), cor.getSimilarityScore()));
//            logger.info(String.format("'%s' <-> '%s' (%.4f)", cor.getFirstRecord().getName(), cor.getSecondRecord().getName(), cor.getSimilarityScore()));
            if(cor.getCausalCorrespondences()!=null) {
                for(Correspondence<MatchableValue, Matchable> cause : cor.getCausalCorrespondences().get()) {
//                    logger.info(String.format("%s (%.4f), ", cause.getFirstRecord().getValue(), cause.getSimilarityScore()));
                        System.out.println(String.format("%s (%.4f), ", cause.getFirstRecord().getValue(), cause.getSimilarityScore()));
                }
//                logger.info("");
            }
            System.out.println("\n");

        }
    }

    public static void labelBased() throws Exception {

        CSVReader reader = new CSVReader(new FileReader("gs_offers_kvp.csv"));
        reader.readNext(); // read the header and ignore it
        String[] line; // store one line of offer

        // process each offer iteratively
        while ((line = reader.readNext()) != null) {

            //--------------------- create a csv out of each offer -----------------------
            String node_id = line[1];
            String url = line[0];
            String kvp = line[2];
            if (kvp.length() == 0) {
                continue;
            }
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
                File file = new File("./goldstandard.csv");
                FileWriter writer2 = new FileWriter(file, true);
                BufferedWriter br = new BufferedWriter(writer2);
                br.write(node_id + "," + url + "," + String.format("'%s','%s'", cor.getFirstRecord().getName(), cor.getSecondRecord().getName()) + "\n");
                br.close();
                writer2.close();
            }
        }
    }
}
