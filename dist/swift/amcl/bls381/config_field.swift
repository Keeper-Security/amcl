public struct CONFIG_FIELD{
    static public let NOT_SPECIAL=0
    static public let PSEUDO_MERSENNE=1
    static public let MONTGOMERY_FRIENDLY=2
    static public let GENERALISED_MERSENNE=3

    static public let MODBITS:UInt = 381
    static let MOD8:UInt = 3
    static public let MODTYPE =  NOT_SPECIAL   

    static let FEXCESS:Int32 = ((Int32(1)<<25)-1)
    static let OMASK:Chunk=Chunk(-1)<<Chunk(CONFIG_FIELD.MODBITS%CONFIG_BIG.BASEBITS)
    static let TBITS:UInt=CONFIG_FIELD.MODBITS%CONFIG_BIG.BASEBITS; // Number of active bits in top word
    static let TMASK:Chunk=(1<<Chunk(CONFIG_FIELD.TBITS))-1

}