import java.io.File;
import java.util.HashMap;
import java.util.Map;

import org.slf4j.Logger;

import de.uni_mannheim.informatik.dws.winter.model.DataSet;
import de.uni_mannheim.informatik.dws.winter.model.HashedDataSet;
import de.uni_mannheim.informatik.dws.winter.model.defaultmodel.Attribute;
import de.uni_mannheim.informatik.dws.winter.model.defaultmodel.CSVRecordReader;
import de.uni_mannheim.informatik.dws.winter.model.defaultmodel.Record;
import de.uni_mannheim.informatik.dws.winter.model.defaultmodel.RecordCSVFormatter;
import de.uni_mannheim.informatik.dws.winter.model.defaultmodel.preprocessing.DataSetNormalizer;
import de.uni_mannheim.informatik.dws.winter.usecase.countries.model.Country;
import de.uni_mannheim.informatik.dws.winter.utils.WinterLogManager;
import de.uni_mannheim.informatik.dws.winter.webtables.detectors.PatternbasedTypeDetector;

public class DataNormalization_DefaultModel {

    String[] str = "id","title","studio","movie genre","budget","gross","director","date"

    DataSet<Record, Attribute> data1 = new HashedDataSet<>();
    new CSVRecordReader(0).loadFromCSV(new File("scifi1.csv"), data1);
    DataSet<Record, Attribute> data2 = new HashedDataSet<>();
    new CSVRecordReader(0).loadFromCSV(new File("scifi2.csv"), data2);

    // Initialize Matching Engine
    MatchingEngine<Record, Attribute> engine = new MatchingEngine<>();
    // run the matching
    Processable<Correspondence<Attribute, Record>> correspondences
            = engine.runLabelBasedSchemaMatching(data1.getSchema(), data2.getSchema(), new LabelComparatorJaccard(), 0.5);

    for(Correspondence<Attribute, Record> cor : correspondences.get()) {
        System.out.println(String.format("'%s' <-> '%s' (%.4f)",
                cor.getFirstRecord().getName(),
                cor.getSecondRecord().getName(),
                cor.getSimilarityScore()));
    }
}