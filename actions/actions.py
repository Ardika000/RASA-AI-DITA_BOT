# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType
from rasa_sdk.types import DomainDict
from datetime import datetime
import locale

def set_locale_to_indonesian():
    try:
        locale.setlocale(locale.LC_TIME, "id_ID.UTF-8")
    except locale.Error:
        locale.setlocale(locale.LC_TIME, "id_ID")

guru_dictionary={
    "guru":{
        "TJKT":{
            "matematika":{
                "10":"Mam Wahyu",
                "11":"Mam Santi",
                "12":"Mam Diah"
            },
            "b.indonesia":{
                "10":"Pak Ario",
                "11":"Mam Dhita",
                "12":"Pak Ario"
            },
            "b.jawa":{
                "10":"Mam Erna"
            },
            "b.inggris":{
                "10":"Mam Jelisha",
                "11":"Mam Jelisha",
                "12":"Mam Kris",
            },
            "pp":{
                "10":"Mam Wuri",
                "11":"Pak Erwin",
                "12":"Pak Luhur"
            },
            "pai":{
                "10":"Pak Slamet",
                "11":"Pak Slamet",
                "12":"Pak Marno"
            },
            "ipas":{
                "10":"Pak Sigid"
            },
            "dtjkt":{
                "10":"Pak Slamet"
            },
            "pkk":{
                "11":"Mam Linda",
                "12":"Mam Cantika"
            },
            "olahraga":{
                "10":"Pak Suparno",
                "11":"Pak Gatot",
                "12":"Pak Adi"
            }

        },
        "KA":{
            "matematika":{
                "10":"Mam Wahyu",
                "11":"Mam Santi",
                "12":"Mam Diah"
            },
            "b.indonesia":{
                "10":"Pak Ario",
                "11":"Mam Dhita",
                "12":"Pak Ario"
            },
            "b.jawa":{
                "10":"Mam Erna"
            },
            "b.inggris":{
                "10":"Mam Jelisha",
                "11":"Mam Jelisha",
                "12":"Mam Kris",
            },
            "pp":{
                "10":"Mam Wuri",
                "11":"Pak Erwin",
                "12":"Pak Luhur"
            },
            "pai":{
                "10":"Pak Slamet",
                "11":"Pak Slamet",
                "12":"Pak Marno"
            },
            "ipas":{
                "10":"Pak Sigid"
            },
            "dtjkt":{
                "10":"Pak Slamet"
            },
            "pkk":{
                "11":"Mam Linda",
                "12":"Mam Cantika"
            },
            "olahraga":{
                "10":"Pak Suparno",
                "11":"Pak Gatot",
                "12":"Pak Adi"
            }

        },
        "DKV":{
            "matematika":{
                "10":"Mam Wahyu",
                "11":"Mam Santi",
                "12":"Mam Diah"
            },
            "b.indonesia":{
                "10":"Pak Ario",
                "11":"Mam Dhita",
                "12":"Pak Ario"
            },
            "b.jawa":{
                "10":"Mam Erna"
            },
            "b.inggris":{
                "10":"Mam Jelisha",
                "11":"Mam Jelisha",
                "12":"Mam Kris",
            },
            "pp":{
                "10":"Mam Wuri",
                "11":"Pak Erwin",
                "12":"Pak Luhur"
            },
            "pai":{
                "10":"Pak Slamet",
                "11":"Pak Slamet",
                "12":"Pak Marno"
            },
            "ipas":{
                "10":"Pak Sigid"
            },
            "dtjkt":{
                "10":"Pak Slamet"
            },
            "pkk":{
                "11":"Mam Linda",
                "12":"Mam Cantika"
            },
            "olahraga":{
                "10":"Pak Suparno",
                "11":"Pak Gatot",
                "12":"Pak Adi"
            }

        },
        "OTO":{
            "matematika":{
                "10":"Mam Wahyu",
                "11":"Mam Santi",
                "12":"Mam Diah"
            },
            "b.indonesia":{
                "10":"Pak Ario",
                "11":"Mam Dhita",
                "12":"Pak Ario"
            },
            "b.jawa":{
                "10":"Mam Erna"
            },
            "b.inggris":{
                "10":"Mam Jelisha",
                "11":"Mam Jelisha",
                "12":"Mam Kris",
            },
            "pp":{
                "10":"Mam Wuri",
                "11":"Pak Erwin",
                "12":"Pak Luhur"
            },
            "pai":{
                "10":"Pak Slamet",
                "11":"Pak Slamet",
                "12":"Pak Marno"
            },
            "ipas":{
                "10":"Pak Sigid"
            },
            "dtjkt":{
                "10":"Pak Slamet"
            },
            "pkk":{
                "11":"Mam Linda",
                "12":"Mam Cantika"
            },
            "olahraga":{
                "10":"Pak Suparno",
                "11":"Pak Gatot",
                "12":"Pak Adi"
            }

        },
        "TM":{
            "matematika":{
                "10":"Mam Wahyu",
                "11":"Mam Santi",
                "12":"Mam Diah"
            },
            "b.indonesia":{
                "10":"Pak Ario",
                "11":"Mam Dhita",
                "12":"Pak Ario"
            },
            "b.jawa":{
                "10":"Mam Erna"
            },
            "b.inggris":{
                "10":"Mam Jelisha",
                "11":"Mam Jelisha",
                "12":"Mam Kris",
            },
            "pp":{
                "10":"Mam Wuri",
                "11":"Pak Erwin",
                "12":"Pak Luhur"
            },
            "pai":{
                "10":"Pak Slamet",
                "11":"Pak Slamet",
                "12":"Pak Marno"
            },
            "ipas":{
                "10":"Pak Sigid"
            },
            "dtjkt":{
                "10":"Pak Slamet"
            },
            "pkk":{
                "11":"Mam Linda",
                "12":"Mam Cantika"
            },
            "olahraga":{
                "10":"Pak Suparno",
                "11":"Pak Gatot",
                "12":"Pak Adi"
            }

        },
        "LAS":{
            "matematika":{
                "10":"Mam Wahyu",
                "11":"Mam Santi",
                "12":"Mam Diah"
            },
            "b.indonesia":{
                "10":"Pak Ario",
                "11":"Mam Dhita",
                "12":"Pak Ario"
            },
            "b.jawa":{
                "10":"Mam Erna"
            },
            "b.inggris":{
                "10":"Mam Jelisha",
                "11":"Mam Jelisha",
                "12":"Mam Kris",
            },
            "pp":{
                "10":"Mam Wuri",
                "11":"Pak Erwin",
                "12":"Pak Luhur"
            },
            "pai":{
                "10":"Pak Slamet",
                "11":"Pak Slamet",
                "12":"Pak Marno"
            },
            "ipas":{
                "10":"Pak Sigid"
            },
            "dtjkt":{
                "10":"Pak Slamet"
            },
            "pkk":{
                "11":"Mam Linda",
                "12":"Mam Cantika"
            },
            "olahraga":{
                "10":"Pak Suparno",
                "11":"Pak Gatot",
                "12":"Pak Adi"
            }
        }

    }
}

data_dictionary={
    "profil_sekolah":"SMK Tunas Harapan Pati didirikan oleh Yayasan Tunas Harapan Bangsa Pati pada tahun 1990. SMK Tunas Harapan Pati didirikan berdasarkan SK 845/103/90 tanggal 20 Juni 1990, dengan kepala Sekolah Drs. Mu’alim. Pada tahun 1993 kepala Sekolah di ganti oleh Ir. Eny Wahyuningsih dan menjabat sampai sekarang.",
    "produk":"1. Blok Mesin(TM)\n2. Sabun Cupi(KA)\n3. Gantungan Kunci(DKV)",
    "TJKT":{
        "kerja": "1. Network Enginner\n2. Teknisi IT Center\n3. Software Engginer\n4. IT Support\n5. UI/UX Desainer\n6. Syslog Server\n7. Industri Internet Service Provider\n8. Software Developer\n9. IT Consultant",
        "profil":"Teknik Jaringan Komputer dan Telekomunikasi (TJKT) merupakan salah satu program keahlian SMK yang bergerak di bidang Informasi dan Teknologi. Belajar mengenai teknologi informasi siswa dan siswi jurusan TJKT dididik untuk mampu melakukan installasi jaringan komputer, baik itu jaringan komputer dalam rumah / kantor, antar kantor, antar kota, antar provinsi, bahkan antar negara. Dengan kurikulum merdeka jurusan Teknik Jaringan Komputer dan Telekomunikasi (TJKT) yang dulunya Namanya adalah Teknik Komputer dan Jaringan (TKJ) berubah pula struktur kurikulum yang kami gunakan di jurunan TJKT, tidak hanya belajar tentang jaringan namun juga belajar tentang pemprograman. Membuat berbagai program mulai dari yang paling sederhana, membuat game interaktif sampai dengan membuat aplikasi untuk perkantoran dan pertokoan.",
        "materi":"1. Profesi dan Proses Bisnis di bidan Teknik jaringan Komputer dan Telekomunikasi\n2. Dasar Desain Pemprograman\n3. Pemprograman Web menggunakan framework\n4. Pemprograman Mobile (membuat aplikasi android)\n5. Infrastruktur Jaringan (kabel dan nirkabel)\n6. Cloud Computing\n7. Kewirausahaan di bidan Teknik jaringan Komputer dan Telekomunikasi\n8. Dasar Komputer dan perbaikan\n9. Pemprograman Desktop menggunakan Bahasa VB\n10. Perancangan dan pembuatan game interaktif\n11. Sistem Oprasi Jaringan\n12. Dasar Desain Grafis\n13. Pemprograman berbasis Web\n14. Pemprograman Desktop menggunakan Bahasa C#\n15. Dasar Jaringan Komputer\n16. Pemprograman Jaringan",
        "jadwal":{
            "10":{
                "senin":{
                    "1":{
                        "materi":"upacara",
                        "guru":"semua",
                        "ruang":"lapangan"
                    },
                    "2":{
                        "materi":"IPAS_KIM",
                        "guru":"Pak Sigit",
                        "ruang":"YTA"
                    },
                    "3":{
                        "materi":"IPAS_KIM",
                        "guru":"Pak Sigit",
                        "ruang":"YTA"
                    },
                    "4":{
                        "materi":"Matematika",
                        "guru":"Mam Wahyuning",
                        "ruang":"A.111"
                    },
                    "5":{
                        "materi":"Matematika",
                        "guru":"Mam Wahyuning",
                        "ruang":"A.111"
                    },
                    "6":{
                        "materi":"IPAS_KIM",
                        "guru":"Pak Sigit",
                        "ruang":"YTA"
                    },
                    "7":{
                        "materi":"IPAS_KIM",
                        "guru":"Pak Sigit",
                        "ruang":"YTA"
                    }
                },
                "selasa":{
                    "1":{
                        "materi":"DTJKT",
                        "guru":"Pak Slamet",
                        "ruang":"PERAKITAN"
                    },
                    "2":{
                        "materi":"DTJKT",
                        "guru":"Pak Slamet",
                        "ruang":"PERAKITAN"
                    },
                    "3":{
                        "materi":"DTJKT",
                        "guru":"Pak Slamet",
                        "ruang":"PERAKITAN"
                    },
                    "4":{
                        "materi":"DTJKT",
                        "guru":"Pak Slamet",
                        "ruang":"PERAKITAN"
                    },
                    "5":{
                        "materi":"DTJKT",
                        "guru":"Pak Slamet",
                        "ruang":"PERAKITAN"
                    },
                    "6":{
                        "materi":"DTJKT",
                        "guru":"Pak Slamet",
                        "ruang":"PERAKITAN"
                    },
                },
                "kamis":{
                    "1":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "2":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "3":{
                        "materi":"PKK",
                        "guru": "Mam Cantika",
                        "ruang": "C.113"
                    },
                    "4":{
                        "materi":"PKK",
                        "guru": "Mam Cantika",
                        "ruang": "C.113"
                    },
                    "5":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "6":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "7":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Aryo",
                        "ruang": "B.104"
                    },
                    "8":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Aryo",
                        "ruang": "B.104"
                    },
                    "9":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Aryo",
                        "ruang": "B.104"
                    },
                },
                "jumat":{
                    "1":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "2":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "3":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "4":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "5":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "6":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "7":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "8":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "9":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "10":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "11":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    }
                },
                "sabtu":{
                    "1":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "2":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "3":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "4":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "5":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "6":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "7":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "8":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "9":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "10":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "11":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    }
                },
            },
            "11":{
                "senin":{
                    "1":{
                        "materi":"upacara",
                        "guru":"-",
                        "ruang":"lapangan"
                    },
                    "2":{
                        "materi":"PCC",
                        "guru":"Pak Ryan",
                        "ruang":"PRODESK"
                    },
                    "3":{
                        "materi":"PCC",
                        "guru":"Pak Ryan",
                        "ruang":"PRODESK"
                    },
                    "4":{
                        "materi":"PCC",
                        "guru":"Pak Ryan",
                        "ruang":"PRODESK"
                    },
                    "5":{
                        "materi":"PCC",
                        "guru":"Pak Ryan",
                        "ruang":"PRODESK"
                    },
                    "6":{
                        "materi":"PCC",
                        "guru":"Pak Ryan",
                        "ruang":"PRODESK"
                    },
                    "7":{
                        "materi":"PCC",
                        "guru":"Pak Ryan",
                        "ruang":"PRODESK"
                    },
                    "8":{
                        "materi":"PCC",
                        "guru":"Pak Ryan",
                        "ruang":"PRODESK"
                    },
                    "9":{
                        "materi":"PCC",
                        "guru":"Pak Ryan",
                        "ruang":"PRODESK"
                    },
                    "10":{
                        "materi":"PCC",
                        "guru":"Pak Ryan",
                        "ruang":"PRODESK"
                    },
                },
                "selasa":{
                    "3":{
                        "materi":"olahraga",
                        "guru":"Pak Gatot",
                        "ruang":"Lapangan"
                    },
                    "4":{
                        "materi":"olahraga",
                        "guru":"Pak Gatot",
                        "ruang":"Lapangan"
                    },
                    "5":{
                        "materi":"Olahraga",
                        "guru":"Pak Gatot",
                        "ruang":"Lapangan"
                    },
                    "6":{
                        "materi":"BK",
                        "guru":"Pak Sugiarto",
                        "ruang":"C.214"
                    },
                    "7":{
                        "materi":"PP",
                        "guru":"Pak Erwin",
                        "ruang":"D.104"
                    },
                    "8":{
                        "materi":"PP",
                        "guru":"Pak Erwin",
                        "ruang":"D.104"
                    },
                    "9":{
                        "materi":"PP",
                        "guru":"Pak Erwin",
                        "ruang":"D.104"
                    }
                },
                "rabu":{
                    "3":{
                        "materi":"Matematika",
                        "guru":"Mam Santi",
                        "ruang":"C.214"
                    },
                    "4":{
                        "materi":"Matematika",
                        "guru":"Mam Santi",
                        "ruang":"C.214"
                    },
                    "5":{
                        "materi":"B. Indonesia",
                        "guru":"Mam Dhita",
                        "ruang":"C.113"
                    },
                    "6":{
                        "materi":"B. Indonesia",
                        "guru":"Mam Dhita",
                        "ruang":"C.113"
                    },
                    "7":{
                        "materi":"Project PKK",
                        "guru":"Pak Sigit",
                        "ruang":"Lab Fisika"
                    },
                    "8":{
                        "materi":"Project PKK",
                        "guru":"Pak Sigit",
                        "ruang":"Lab Fisika"
                    },
                    "9":{
                        "materi":"Project PKK",
                        "guru":"Pak Sigit",
                        "ruang":"Lab Fisika"
                    }
                },
                "Kamis":{
                    "1":{
                        "materi":"PIC",
                        "guru":"Pak Dimas",
                        "ruang":"Cisco E"
                    },
                    "2":{
                        "materi":"PIC",
                        "guru":"Pak Dimas",
                        "ruang":"Cisco E"
                    },
                    "3":{
                        "materi":"PIC",
                        "guru":"Pak Dimas",
                        "ruang":"Cisco E"
                    },
                    "4":{
                        "materi":"PIC",
                        "guru":"Pak Dimas",
                        "ruang":"Cisco E"
                    },
                    "5":{
                        "materi":"PIC",
                        "guru":"Pak Dimas",
                        "ruang":"Cisco E"
                    },
                    "6":{
                        "materi":"PIC",
                        "guru":"Pak Dimas",
                        "ruang":"Cisco E"
                    },
                    "7":{
                        "materi":"PIC",
                        "guru":"Pak Dimas",
                        "ruang":"Cisco E"
                    },
                    "8":{
                        "materi":"PIC",
                        "guru":"Pak Dimas",
                        "ruang":"Cisco E"
                    },
                    "9":{
                        "materi":"PIC",
                        "guru":"Pak Dimas",
                        "ruang":"Cisco E"
                    },
                    "10":{
                        "materi":"PIC",
                        "guru":"Pak Dimas",
                        "ruang":"Cisco E"
                    },
                },
                "Jumat":{
                    "1":{
                        "materi":"B. Indonesia",
                        "guru": "Mam Dhita",
                        "ruang": "C.113"
                    },
                    "2":{
                        "materi":"B. Indonesia",
                        "guru": "Mam Dhita",
                        "ruang": "C.113"
                    },
                    "3":{
                        "materi":"B. Inggris",
                        "guru": "Mam Jelisha",
                        "ruang": "D.301"
                    },
                    "4":{
                        "materi":"B. Inggris",
                        "guru": "Mam Jelisha",
                        "ruang": "D.301"
                    },
                    "5":{
                        "materi":"PKK",
                        "guru": "Mam Linda",
                        "ruang": "D.101"
                    },
                    "6":{
                        "materi":"PKK",
                        "guru": "Mam Linda",
                        "ruang": "D.101"
                    },
                    "8":{
                        "materi":"Matematika",
                        "guru": "Mam Santi",
                        "ruang": "C.214"
                    },
                    "9":{
                        "materi":"Matematika",
                        "guru": "Mam Santi",
                        "ruang": "C.214"
                    },
                    "10":{
                        "materi":"Matematika",
                        "guru": "Mam Santi",
                        "ruang": "C.214"
                    },
                },
                "sabtu":{
                    "1":{
                        "materi":"B. Inggris",
                        "guru": "Mam Jelisha",
                        "ruang": "D.301"
                    },
                    "2":{
                        "materi":"B. Inggris",
                        "guru": "Mam Jelisha",
                        "ruang": "D.301"
                    },
                    "3":{
                        "materi":"B. Inggris",
                        "guru": "Mam Jelisha",
                        "ruang": "D.301"
                    },
                    "4":{
                        "materi":"PAI",
                        "guru": "Pak Slamet",
                        "ruang": "C.114"
                    },
                    "5":{
                        "materi":"PAI",
                        "guru": "Pak Slamet",
                        "ruang": "C.114"
                    },
                    "6":{
                        "materi":"PAI",
                        "guru": "Pak Slamet",
                        "ruang": "C.114"
                    },
                    "7":{
                        "materi":"Sejarah",
                        "guru": "Pak Aris",
                        "ruang": "B.305"
                    },
                    "8":{
                        "materi":"Sejarah",
                        "guru": "Pak Aris",
                        "ruang": "B.305"
                    }
                },

            },
            "12":{
                "senin":{
                    "1":{
                        "materi":"upacara",
                        "guru":"-",
                        "ruang":"lapangan"
                    },
                    "2":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "3":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "4":{
                        "materi":"PP",
                        "guru":"Pak Luhur",
                        "ruang":"A.109"
                    },
                    "5":{
                        "materi":"PP",
                        "guru":"Pak Luhur",
                        "ruang":"A.109"
                    }
                },
                "selasa":{
                    "1":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "2":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "3":{
                        "materi":"PAI",
                        "guru":"Pak Marno",
                        "ruang":"B.103"
                    },
                    "4":{
                        "materi":"PAI",
                        "guru":"Pak Marno",
                        "ruang":"B.103"
                    },
                    "5":{
                        "materi":"BK",
                        "guru":"Mam Ayunda",
                        "ruang":"A.109"
                    },
                },
                "kamis":{
                    "1":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "2":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "3":{
                        "materi":"PKK",
                        "guru": "Mam Cantika",
                        "ruang": "C.113"
                    },
                    "4":{
                        "materi":"PKK",
                        "guru": "Mam Cantika",
                        "ruang": "C.113"
                    },
                    "5":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "6":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "7":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Aryo",
                        "ruang": "B.104"
                    },
                    "8":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Aryo",
                        "ruang": "B.104"
                    },
                    "9":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Aryo",
                        "ruang": "B.104"
                    },
                },
                "jumat":{
                    "1":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "2":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "3":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "4":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "5":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "6":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "8":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "9":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "10":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "11":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    }
                },
                "sabtu":{
                    "1":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "2":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "3":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "4":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "5":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "6":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "7":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "8":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "9":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "10":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "11":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    }
                },
            },
        }
    },
    "KA":{
        "kerja": "1. PT. Inti Celulose Indonesia\n2. PT. Suntory\n3. PT. Phapros\n4. PT. Pura Barutama\n5. Balai Lingkungan Hidup Pati\n6. PT. Garuda Food\n7. PT. Dua Kelinci\n8. PT. Arkof\n9. PT. GS Battery",
        "profil":"Kimia Analisis adalah cabang kimia yang berhubungan dengan pengembangan dan penggunaan teknik untuk pengukuran kimia. Kimiawan menggunakan teknik-teknik untuk menentukan komposisi kimia suatu zat. Kimia analisis bisa bersifat kualitatif atau kuantitatif. Analisis kualitatif mengidentifikasi unsur-unsur atau senyawa yang membentuk zat. Analisis kuantitatif mengukur jumlah beberapa atau semua elemen atau senyawa. Kimia analisis memberikan informasi penting untuk ilmu pengetahuan dan industri. Misalnya, kimia analisis digunakan untuk menguji sampel makanan, tanah, dan air untuk mengidentifikasi kandungan kimia. Industri pangan menggunakan metode analisis menguji bahan baku dan produk dalam makanan, obat, dan bahan industri lainnya sebagai kontrol kualitas. Laboratorium pengujian menggunakan teknik analisis untuk memeriksa sampel sesuai kebutuhan klien termasuk uji mikrobiologis seperti uji kapang, jamur dan bakteri.",
        "materi":"1. Proses bisnis secara menyeluruh bidang kimia analisis\n2. Teknik dasar proses kerja di bidang kimia analisis\n3. Pengelolaan Peralatan Laboratorium\n4. Pengambilan dan Penyiapan Sampel\n5. Analisis Kimia Instrumen\n6. Perkembangan teknologi di dunia kerja dan isu-isu global terkait kimia analisis\n7. Keselamatan dan Kesehatan Kerja serta Lingkungan Hidup (K3LH) dan budaya kerja industri\n8. Larutan Standar\n9. Analisis Titrimetri dan Gravimetri\n10. Analisis Mikrobiologi\n11. Profesi dan kewirausahaan dan peluang usaha di bidang kimia analisis\n12. Pengelolaan Laboratorium Kimia\n13. Analisis Kualitatif dan Kuantitatif Sederhana\n14. Analisis Proksimat",
        "jadwal":{
            "10":{
                "senin":{
                    "1":{
                        "materi":"upacara",
                        "guru":"semua",
                        "ruang":"lapangan"
                    },
                    "2":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "3":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "4":{
                        "materi":"PP",
                        "guru":"Pak Luhur",
                        "ruang":"A.109"
                    },
                    "5":{
                        "materi":"PP",
                        "guru":"Pak Luhur",
                        "ruang":"A.109"
                    }
                },
                "selasa":{
                    "1":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "2":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "3":{
                        "materi":"PAI",
                        "guru":"Pak Marno",
                        "ruang":"B.103"
                    },
                    "4":{
                        "materi":"PAI",
                        "guru":"Pak Marno",
                        "ruang":"B.103"
                    },
                    "5":{
                        "materi":"BK",
                        "guru":"Mam Ayunda",
                        "ruang":"A.109"
                    },
                },
                "kamis":{
                    "1":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "2":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "3":{
                        "materi":"PKK",
                        "guru": "Mam Cantika",
                        "ruang": "C.113"
                    },
                    "4":{
                        "materi":"PKK",
                        "guru": "Mam Cantika",
                        "ruang": "C.113"
                    },
                    "5":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "6":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "7":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Aryo",
                        "ruang": "B.104"
                    },
                    "8":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Aryo",
                        "ruang": "B.104"
                    },
                    "9":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Aryo",
                        "ruang": "B.104"
                    },
                },
                "jumat":{
                    "1":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "2":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "3":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "4":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "5":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "6":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "7":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "8":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "9":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "10":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "11":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    }
                },
                "sabtu":{
                    "1":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "2":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "3":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "4":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "5":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "6":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "7":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "8":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "9":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "10":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "11":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    }
                },
            },
            "11":{
                "senin":{
                    "1":{
                        "materi":"upacara",
                        "guru":"-",
                        "ruang":"lapangan"
                    },
                    "2":{
                        "materi":"B. Inggris",
                        "guru":"Miss Alrina",
                        "ruang":"D.205"
                    },
                    "3":{
                        "materi":"B. Inggris",
                        "guru":"Miss Alrina",
                        "ruang":"D.205"
                    },
                    "4":{
                        "materi":"Olahraga",
                        "guru":"Pak Gatot",
                        "ruang":"Lapangan"
                    },
                    "5":{
                        "materi":"Olahraga",
                        "guru":"Pak Gatot",
                        "ruang":"Lapangan"
                    },
                    "6":{
                        "materi":"PKK",
                        "guru":"Mam Linda",
                        "ruang":"D.101"
                    },
                    "7":{
                        "materi":"PKK",
                        "guru":"Mam Linda",
                        "ruang":"D.101"
                    },
                    "8":{
                        "materi":"Matematika",
                        "guru":"Mam Ika",
                        "ruang":"C.213"
                    },
                    "9":{
                        "materi":"Matematika",
                        "guru":"Mam Ika",
                        "ruang":"C.213"
                    }
                },
                "selasa":{
                    "1":{
                        "materi":"Matematika",
                        "guru":"Mam Ika",
                        "ruang":"C.213"
                    },
                    "2":{
                        "materi":"Matematika",
                        "guru":"Mam Ika",
                        "ruang":"C.213"
                    },
                    "3":{
                        "materi":"PP",
                        "guru":"Pak Erwin",
                        "ruang":"D.104"
                    },
                    "4":{
                        "materi":"PP",
                        "guru":"Pak Erwin",
                        "ruang":"D.104"
                    },
                    "5":{
                        "materi":"B. Indonesia",
                        "guru":"Pak Sobiron",
                        "ruang":"D.202"
                    },
                    "6":{
                        "materi":"B. Indonesia",
                        "guru":"Pak Sobiron",
                        "ruang":"D.202"
                    },
                    "7":{
                        "materi":"B. Indonesia",
                        "guru":"Pak Sobiron",
                        "ruang":"D.202"
                    },
                    "8":{
                        "materi":"BK",
                        "guru":"Mam Andhini",
                        "ruang":"C.213"
                    },
                },
                "Rabu":{
                    "3":{
                        "materi":"B. Inggris",
                        "guru":"Miss Alrina",
                        "ruang":"D.205"
                    },
                    "4":{
                        "materi":"B. Inggris",
                        "guru":"Miss Alrina",
                        "ruang":"D.205"
                    },
                    "5":{
                        "materi":"PAI",
                        "guru":"Pak Slamet",
                        "ruang":"C.114"
                    },
                    "6":{
                        "materi":"PAI",
                        "guru":"Pak Slamet",
                        "ruang":"C.114"
                    },
                    "7":{
                        "materi":"Sejarah",
                        "guru":"Pak Aris",
                        "ruang":"B.305"
                    },
                    "8":{
                        "materi":"Sejarah",
                        "guru":"Pak Aris",
                        "ruang":"B.305"
                    },
                },
                "kamis":{
                    "1":{
                        "materi":"AP",
                        "guru": "Mam Ratnasari",
                        "ruang": "LAB 1"
                    },
                    "2":{
                        "materi":"AP",
                        "guru": "Mam Ratnasari",
                        "ruang": "LAB 1"
                    },
                    "3":{
                        "materi":"AP",
                        "guru": "Mam Ratnasari",
                        "ruang": "LAB 1"
                    },
                    "4":{
                        "materi":"AP",
                        "guru": "Mam Ratnasari",
                        "ruang": "LAB 1"
                    },
                    "5":{
                        "materi":"AP",
                        "guru": "Mam Ratnasari",
                        "ruang": "LAB 1"
                    },
                    "6":{
                        "materi":"AI 2",
                        "guru": "Pak Ali",
                        "ruang": "LAB 4"
                    },
                    "7":{
                        "materi":"AI 2",
                        "guru": "Pak Ali",
                        "ruang": "LAB 4"
                    },
                    "8":{
                        "materi":"AI 2",
                        "guru": "Pak Ali",
                        "ruang": "LAB 4"
                    },
                    "9":{
                        "materi":"AI 2",
                        "guru": "Pak Ali",
                        "ruang": "LAB 4"
                    },
                    "10":{
                        "materi":"AI 2",
                        "guru": "Pak Ali",
                        "ruang": "LAB 4"
                    },
                },
                "jumat":{
                    "2":{
                        "materi":"AKK TITRASI",
                        "guru": "Mam Irma",
                        "ruang": "LAB 4"
                    },
                    "3":{
                        "materi":"AKK TITRASI",
                        "guru": "Mam Irma",
                        "ruang": "LAB 4"
                    },
                    "4":{
                        "materi":"AKK TITRASI",
                        "guru": "Mam Irma",
                        "ruang": "LAB 4"
                    },
                    "5":{
                        "materi":"AKK TITRASI",
                        "guru": "Mam Irma",
                        "ruang": "LAB 4"
                    },
                    "6":{
                        "materi":"AKK TITRASI",
                        "guru": "Mam Irma",
                        "ruang": "LAB 4"
                    },
                    "8":{
                        "materi":"AM",
                        "guru": "Pak Sigit",
                        "ruang": "LAB 2"
                    },
                    "9":{
                        "materi":"AM",
                        "guru": "Pak Sigit",
                        "ruang": "LAB 2"
                    },
                    "10":{
                        "materi":"AM",
                        "guru": "Pak Sigit",
                        "ruang": "LAB 2"
                    },
                    "11":{
                        "materi":"AM",
                        "guru": "Pak Sigit",
                        "ruang": "LAB 2"
                    },
                    "12":{
                        "materi":"AM",
                        "guru": "Pak Sigit",
                        "ruang": "LAB 2"
                    }
                },
                "sabtu":{
                    "1":{
                        "materi":"GRAVI",
                        "guru": "Mam Endang",
                        "ruang": "LAB 3"
                    },
                    "2":{
                        "materi":"GRAVI",
                        "guru": "Mam Endang",
                        "ruang": "LAB 3"
                    },
                    "3":{
                        "materi":"GRAVI",
                        "guru": "Mam Endang",
                        "ruang": "LAB 3"
                    },
                    "4":{
                        "materi":"GRAVI",
                        "guru": "Mam Endang",
                        "ruang": "LAB 3"
                    },
                    "5":{
                        "materi":"GRAVI",
                        "guru": "Mam Endang",
                        "ruang": "LAB 3"
                    },
                    "6":{
                        "materi":"GRAVI",
                        "guru": "Mam Endang",
                        "ruang": "LAB 3"
                    },
                    "7":{
                        "materi":"GRAVI",
                        "guru": "Mam Endang",
                        "ruang": "LAB 3"
                    }
                },

            },
            "12":{
                "senin":{
                    "1":{
                        "materi":"upacara",
                        "guru":"-",
                        "ruang":"lapangan"
                    },
                    "2":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "3":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "4":{
                        "materi":"PP",
                        "guru":"Pak Luhur",
                        "ruang":"A.109"
                    },
                    "5":{
                        "materi":"PP",
                        "guru":"Pak Luhur",
                        "ruang":"A.109"
                    }
                },
                "selasa":{
                    "1":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "2":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "3":{
                        "materi":"PAI",
                        "guru":"Pak Marno",
                        "ruang":"B.103"
                    },
                    "4":{
                        "materi":"PAI",
                        "guru":"Pak Marno",
                        "ruang":"B.103"
                    },
                    "5":{
                        "materi":"BK",
                        "guru":"Mam Ayunda",
                        "ruang":"A.109"
                    },
                },
                "kamis":{
                    "1":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "2":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "3":{
                        "materi":"PKK",
                        "guru": "Mam Cantika",
                        "ruang": "C.113"
                    },
                    "4":{
                        "materi":"PKK",
                        "guru": "Mam Cantika",
                        "ruang": "C.113"
                    },
                    "5":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "6":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "7":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Aryo",
                        "ruang": "B.104"
                    },
                    "8":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Aryo",
                        "ruang": "B.104"
                    },
                    "9":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Aryo",
                        "ruang": "B.104"
                    },
                },
                "jumat":{
                    "1":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "2":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "3":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "4":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "5":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "6":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "7":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "8":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "9":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "10":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "11":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    }
                },
                "sabtu":{
                    "1":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "2":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "3":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "4":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "5":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "6":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "7":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "8":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "9":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "10":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "11":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    }
                },
            },
        }
    },
    "DKV":{
        "kerja": "1. Percetakan dan Penerbitan\n2. Periklanan\n3. Desain\n4. Branding\n5. Animator\n6. Ilustrasi\n7. Komik\n8. Creativepreneur",
        "profil":"Desain Komunikasi Visual adalah suatu disiplin ilmu tentang metode penyampaian pesan (komunikasi) dan ungkapan kreatif dengan menggunakan elemen-elemen visual/ rupa/ gambar. Proses kreatif ini menggabungkan seni visual dan teknologi digital. Desain Komunikasi Visual termasuk Bidang Keahlian Seni dan Industri Kreatif. Di sini siswa akan belajar untuk dapat mengolah pesan secara informatif, komunikatif, dan efektif, serta sekreatif mungkin agar pesan dapat mencapai sasaran dengan memperhatikan unsur bentuk, warna, tekstur, ruang, huruf, dan segala hal yang berkaitan dengan visual (pengelihatan). Ilmu yang dipelajari sangat berguna untuk menyesuaikan perkembangan teknologi multimedia digital di masa depan. Program Keahlian Desain Komunikasi Visual SMK Tunas Harapan Pati juga menerapkan pembelajaran TEFA (Teaching Factory), dimana sekolah menerima Job atau orderan dari luar yang nantinya akan dikerjakan oleh siswa, dengan tujuan siswa mendapat pengalaman langsung dalam mengerjakan job dari industri.",
        "materi":"1. Profesi Technopreneur dan Creativepreneur Desain Komunikasi Visual\n2. Teknik Animasi 2 Dimensi\n3. Fotografi\n4. Virtual Reality\n5. Teknologi Desain Grafis\n6. Kewirausahaan Desain Komunikasi Visual\n7. Gambar Sketsa dan Ilustasi\n8. Desain Multimedia Interaktif Berbasis Android\n9. Teknik Animasi 3 Dimensi\n10. Videografi\n11. Augmented Reality\n12. Konten Kreatif",
        "jadwal":{
            "10":{
                "senin":{
                    "1":{
                        "materi":"upacara",
                        "guru":"semua",
                        "ruang":"lapangan"
                    },
                    "2":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "3":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "4":{
                        "materi":"PP",
                        "guru":"Pak Luhur",
                        "ruang":"A.109"
                    },
                    "5":{
                        "materi":"PP",
                        "guru":"Pak Luhur",
                        "ruang":"A.109"
                    }
                },
                "selasa":{
                    "1":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "2":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "3":{
                        "materi":"PAI",
                        "guru":"Pak Marno",
                        "ruang":"B.103"
                    },
                    "4":{
                        "materi":"PAI",
                        "guru":"Pak Marno",
                        "ruang":"B.103"
                    },
                    "5":{
                        "materi":"BK",
                        "guru":"Mam Ayunda",
                        "ruang":"A.109"
                    },
                },
                "kamis":{
                    "1":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "2":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "3":{
                        "materi":"PKK",
                        "guru": "Mam Cantika",
                        "ruang": "C.113"
                    },
                    "4":{
                        "materi":"PKK",
                        "guru": "Mam Cantika",
                        "ruang": "C.113"
                    },
                    "5":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "6":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "7":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Aryo",
                        "ruang": "B.104"
                    },
                    "8":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Aryo",
                        "ruang": "B.104"
                    },
                    "9":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Aryo",
                        "ruang": "B.104"
                    },
                },
                "jumat":{
                    "1":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "2":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "3":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "4":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "5":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "6":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "7":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "8":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "9":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "10":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "11":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    }
                },
                "sabtu":{
                    "1":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "2":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "3":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "4":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "5":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "6":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "7":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "8":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "9":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "10":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "11":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    }
                },
            },
            "11":{
                "senin":{
                    "1":{
                        "materi":"upacara",
                        "guru":"-",
                        "ruang":"lapangan"
                    },
                    "2":{
                        "materi":"B. Inggris",
                        "guru":"Miss Alrina",
                        "ruang":"D.205"
                    },
                    "3":{
                        "materi":"B. Inggris",
                        "guru":"Miss Alrina",
                        "ruang":"D.205"
                    },
                    "4":{
                        "materi":"Olahraga",
                        "guru":"Pak Gatot",
                        "ruang":"Lapangan"
                    },
                    "5":{
                        "materi":"Olahraga",
                        "guru":"Pak Gatot",
                        "ruang":"Lapangan"
                    },
                    "6":{
                        "materi":"PKK",
                        "guru":"Mam Linda",
                        "ruang":"D.101"
                    },
                    "7":{
                        "materi":"PKK",
                        "guru":"Mam Linda",
                        "ruang":"D.101"
                    },
                    "8":{
                        "materi":"Matematika",
                        "guru":"Mam Ika",
                        "ruang":"C.213"
                    },
                    "9":{
                        "materi":"Matematika",
                        "guru":"Mam Ika",
                        "ruang":"C.213"
                    }
                },
                "selasa":{
                    "1":{
                        "materi":"Matematika",
                        "guru":"Mam Ika",
                        "ruang":"C.213"
                    },
                    "2":{
                        "materi":"Matematika",
                        "guru":"Mam Ika",
                        "ruang":"C.213"
                    },
                    "3":{
                        "materi":"PP",
                        "guru":"Pak Erwin",
                        "ruang":"D.104"
                    },
                    "4":{
                        "materi":"PP",
                        "guru":"Pak Erwin",
                        "ruang":"D.104"
                    },
                    "5":{
                        "materi":"B. Indonesia",
                        "guru":"Pak Sobiron",
                        "ruang":"D.202"
                    },
                    "6":{
                        "materi":"B. Indonesia",
                        "guru":"Pak Sobiron",
                        "ruang":"D.202"
                    },
                    "7":{
                        "materi":"B. Indonesia",
                        "guru":"Pak Sobiron",
                        "ruang":"D.202"
                    },
                    "8":{
                        "materi":"BK",
                        "guru":"Mam Andhini",
                        "ruang":"C.213"
                    },
                },
                "Rabu":{
                    "3":{
                        "materi":"B. Inggris",
                        "guru":"Miss Alrina",
                        "ruang":"D.205"
                    },
                    "4":{
                        "materi":"B. Inggris",
                        "guru":"Miss Alrina",
                        "ruang":"D.205"
                    },
                    "5":{
                        "materi":"PAI",
                        "guru":"Pak Slamet",
                        "ruang":"C.114"
                    },
                    "6":{
                        "materi":"PAI",
                        "guru":"Pak Slamet",
                        "ruang":"C.114"
                    },
                    "7":{
                        "materi":"Sejarah",
                        "guru":"Pak Aris",
                        "ruang":"B.305"
                    },
                    "8":{
                        "materi":"Sejarah",
                        "guru":"Pak Aris",
                        "ruang":"B.305"
                    },
                },
                "kamis":{
                    "1":{
                        "materi":"AP",
                        "guru": "Mam Ratnasari",
                        "ruang": "LAB 1"
                    },
                    "2":{
                        "materi":"AP",
                        "guru": "Mam Ratnasari",
                        "ruang": "LAB 1"
                    },
                    "3":{
                        "materi":"AP",
                        "guru": "Mam Ratnasari",
                        "ruang": "LAB 1"
                    },
                    "4":{
                        "materi":"AP",
                        "guru": "Mam Ratnasari",
                        "ruang": "LAB 1"
                    },
                    "5":{
                        "materi":"AP",
                        "guru": "Mam Ratnasari",
                        "ruang": "LAB 1"
                    },
                    "6":{
                        "materi":"AI 2",
                        "guru": "Pak Ali",
                        "ruang": "LAB 4"
                    },
                    "7":{
                        "materi":"AI 2",
                        "guru": "Pak Ali",
                        "ruang": "LAB 4"
                    },
                    "8":{
                        "materi":"AI 2",
                        "guru": "Pak Ali",
                        "ruang": "LAB 4"
                    },
                    "9":{
                        "materi":"AI 2",
                        "guru": "Pak Ali",
                        "ruang": "LAB 4"
                    },
                    "10":{
                        "materi":"AI 2",
                        "guru": "Pak Ali",
                        "ruang": "LAB 4"
                    },
                },
                "jumat":{
                    "2":{
                        "materi":"AKK TITRASI",
                        "guru": "Mam Irma",
                        "ruang": "LAB 4"
                    },
                    "3":{
                        "materi":"AKK TITRASI",
                        "guru": "Mam Irma",
                        "ruang": "LAB 4"
                    },
                    "4":{
                        "materi":"AKK TITRASI",
                        "guru": "Mam Irma",
                        "ruang": "LAB 4"
                    },
                    "5":{
                        "materi":"AKK TITRASI",
                        "guru": "Mam Irma",
                        "ruang": "LAB 4"
                    },
                    "6":{
                        "materi":"AKK TITRASI",
                        "guru": "Mam Irma",
                        "ruang": "LAB 4"
                    },
                    "8":{
                        "materi":"AM",
                        "guru": "Pak Sigit",
                        "ruang": "LAB 2"
                    },
                    "9":{
                        "materi":"AM",
                        "guru": "Pak Sigit",
                        "ruang": "LAB 2"
                    },
                    "10":{
                        "materi":"AM",
                        "guru": "Pak Sigit",
                        "ruang": "LAB 2"
                    },
                    "11":{
                        "materi":"AM",
                        "guru": "Pak Sigit",
                        "ruang": "LAB 2"
                    },
                    "12":{
                        "materi":"AM",
                        "guru": "Pak Sigit",
                        "ruang": "LAB 2"
                    }
                },
                "sabtu":{
                    "1":{
                        "materi":"GRAVI",
                        "guru": "Mam Endang",
                        "ruang": "LAB 3"
                    },
                    "2":{
                        "materi":"GRAVI",
                        "guru": "Mam Endang",
                        "ruang": "LAB 3"
                    },
                    "3":{
                        "materi":"GRAVI",
                        "guru": "Mam Endang",
                        "ruang": "LAB 3"
                    },
                    "4":{
                        "materi":"GRAVI",
                        "guru": "Mam Endang",
                        "ruang": "LAB 3"
                    },
                    "5":{
                        "materi":"GRAVI",
                        "guru": "Mam Endang",
                        "ruang": "LAB 3"
                    },
                    "6":{
                        "materi":"GRAVI",
                        "guru": "Mam Endang",
                        "ruang": "LAB 3"
                    },
                    "7":{
                        "materi":"GRAVI",
                        "guru": "Mam Endang",
                        "ruang": "LAB 3"
                    }
                },

            },
            "12":{
                "senin":{
                    "1":{
                        "materi":"upacara",
                        "guru":"-",
                        "ruang":"lapangan"
                    },
                    "2":{
                        "materi":"DKV RUS",
                        "guru":"Pak Bayu",
                        "ruang":"3D EMMITERLABS"
                    },
                    "3":{
                        "materi":"DKV RUS",
                        "guru":"Pak Bayu",
                        "ruang":"3D EMMITERLABS"
                    },
                    "4":{
                        "materi":"DKV RUS",
                        "guru":"Pak Bayu",
                        "ruang":"3D EMMITERLABS"
                    },
                    "5":{
                        "materi":"DKV RUS",
                        "guru":"Pak Bayu",
                        "ruang":"3D EMMITERLABS"
                    },
                    "6":{
                        "materi":"DKV RUS",
                        "guru":"Pak Bayu",
                        "ruang":"3D EMMITERLABS"
                    },
                    "7":{
                        "materi":"DKV RUS",
                        "guru":"Pak Bayu",
                        "ruang":"3D EMMITERLABS"
                    },
                    "8":{
                        "materi":"DKV RUS",
                        "guru":"Pak Bayu",
                        "ruang":"3D EMMITERLABS"
                    },
                    "9":{
                        "materi":"DKV RUS",
                        "guru":"Pak Bayu",
                        "ruang":"3D EMMITERLABS"
                    },
                    "10":{
                        "materi":"DKV RUS",
                        "guru":"Pak Bayu",
                        "ruang":"3D EMMITERLABS"
                    },
                    "11":{
                        "materi":"DKV RUS",
                        "guru":"Pak Bayu",
                        "ruang":"3D EMMITERLABS"
                    },
                    "12":{
                        "materi":"DKV RUS",
                        "guru":"Pak Bayu",
                        "ruang":"3D EMMITERLABS"
                    },
                },
                "selasa":{
                    "1":{
                        "materi":"DKV GL",
                        "guru":"Pak Aria",
                        "ruang":"LAB STD 4"
                    },
                    "2":{
                        "materi":"DKV GL",
                        "guru":"Pak Aria",
                        "ruang":"LAB STD 4"
                    },
                    "3":{
                        "materi":"DKV GL",
                        "guru":"Pak Aria",
                        "ruang":"LAB STD 4"
                    },
                    "4":{
                        "materi":"DKV GL",
                        "guru":"Pak Aria",
                        "ruang":"LAB STD 4"
                    },
                    "5":{
                        "materi":"DKV GL",
                        "guru":"Pak Aria",
                        "ruang":"LAB STD 4"
                    },
                    "6":{
                        "materi":"DKV GL",
                        "guru":"Pak Aria",
                        "ruang":"LAB STD 4"
                    },
                    "7":{
                        "materi":"DKV GL",
                        "guru":"Pak Aria",
                        "ruang":"LAB STD 4"
                    },
                    "8":{
                        "materi":"DKV GL",
                        "guru":"Pak Aria",
                        "ruang":"LAB STD 4"
                    },
                    "9":{
                        "materi":"DKV GL",
                        "guru":"Pak Aria",
                        "ruang":"LAB STD 4"
                    },
                    "10":{
                        "materi":"DKV GL",
                        "guru":"Pak Aria",
                        "ruang":"LAB STD 4"
                    },
                    "11":{
                        "materi":"DKV GL",
                        "guru":"Pak Aria",
                        "ruang":"LAB STD 4"
                    },
                    "12":{
                        "materi":"DKV GL",
                        "guru":"Pak Aria",
                        "ruang":"LAB STD 4"
                    }
                },
                "rabu":{
                    "1":{
                        "materi":"Matematika",
                        "guru": "Mam Hana",
                        "ruang": "D.302"
                    },
                    "2":{
                        "materi":"Matematika",
                        "guru": "Mam Hana",
                        "ruang": "D.302"
                    },
                    "3":{
                        "materi":"Matematika",
                        "guru": "Mam Hana",
                        "ruang": "D.302"
                    },
                    "4":{
                        "materi":"Matematika",
                        "guru": "Mam Hana",
                        "ruang": "D.302"
                    },
                    "5":{
                        "materi":"BK",
                        "guru": "Mam Andhini",
                        "ruang": "D.303"
                    },
                },
                "kamis":{
                    "1":{
                        "materi":"KK",
                        "guru": "Pak Bayu",
                        "ruang": "B.201"
                    },
                    "2":{
                        "materi":"KK",
                        "guru": "Pak Bayu",
                        "ruang": "B.201"
                    },
                    "3":{
                        "materi":"KK",
                        "guru": "Pak Bayu",
                        "ruang": "B.201"
                    },
                },
                "jumat":{
                    "1":{
                        "materi":"PKK",
                        "guru": "Mam Ine",
                        "ruang": "D.101"
                    },
                    "2":{
                        "materi":"PKK",
                        "guru": "Mam Ine",
                        "ruang": "D.101"
                    },
                    "3":{
                        "materi":"PAI",
                        "guru": "Pak Sueb",
                        "ruang": "C.115"
                    },
                    "4":{
                        "materi":"PAI",
                        "guru": "Pak Sueb",
                        "ruang": "C.115"
                    },
                    "5":{
                        "materi":"B. Inggris",
                        "guru": "Mam Kris",
                        "ruang": "D.204"
                    },
                    "6":{
                        "materi":"B. Inggris",
                        "guru": "Mam Kris",
                        "ruang": "D.204"
                    },
                    "8":{
                        "materi":"B. Indonesia",
                        "guru": "Mam Dhita",
                        "ruang": "B.204"
                    },
                    "9":{
                        "materi":"B. Indonesia",
                        "guru": "Mam Dhita",
                        "ruang": "B.204"
                    },
                    "10":{
                        "materi":"B. Indonesia",
                        "guru": "Mam Dhita",
                        "ruang": "B.204"
                    }
                },
                "sabtu":{
                    "1":{
                        "materi":"B. Inggris",
                        "guru": "Mam Kris",
                        "ruang": "D.204"
                    },
                    "2":{
                        "materi":"B. Inggris",
                        "guru": "Mam Kris",
                        "ruang": "D.204"
                    },
                    "3":{
                        "materi":"PP",
                        "guru": "Pak Erwin",
                        "ruang": "B.206"
                    },
                    "4":{
                        "materi":"PP",
                        "guru": "Pak Erwin",
                        "ruang": "B.206"
                    },
                    "5":{
                        "materi":"Olahraga",
                        "guru": "Pak Sumono",
                        "ruang": "Lapangan"
                    },
                    "6":{
                        "materi":"Olahraga",
                        "guru": "Pak Sumono",
                        "ruang": "Lapangan"
                    }
                },
            },
        }
    },
    "OTO":{
        "kerja": "1. PT. Toyota Manufacturing Indonesia\n2. PT. Astra Daihatsu Motor\n3. PT. Dua Kelinci\n4. PT. GS Battery\n5. CV. New Ratna Motor ( Nasmoco )\n6. PT. Astra Honda Motor\n7. PT. Pamapersada Nusantara\n8. PT. Jiaec\n9. PT. United Tractors\n10. CV. Surya Indah Motor",
        "profil":"Teknik otomotif adalah salah satu cabang ilmu teknik mesin yang mempelajari tentang bagaimana merancang, membuat dan mengembangkan alat-alat transportasi darat yang menggunakan mesin, terutama sepeda motor, mobil, bis dan truk. Teknik otomotif menggabungkan elemen-elemen pengetahuan mekanika, listrik, elektronik, keselamatan dan lingkungan serta matematika, fisika, kimia, biologi dan manajemen. Program studi teknik otomotif di SMK Tunas Harapan Pati dibagi menjadi tiga konsentrasi yakni Teknik kendaraan ringan, Teknik kendaraan berat, Teknik Autobody Repair.",
        "materi":"1. Dasar-dasar otomotif\n2. Perawatan dan Perbaikan Chasis dan Pemindah Tenaga\n3. Perbaikan Panel Body Repair\n4. Model Unit Alat Berat atau Product Knowledge\n5. Sistem Kelistrikan Alat Berat\n6. Perawatan berkala unit Alat Berat\n7. Sistem Pengisian\n8. Sistem Audio\n9. Sistem Pelumas dan Pendingin\n10. Perawatan Berkala sampai dengan 40.000 KM\n11. Sistem Propeler\n12. Sistem Rem Konvensional dan ABS\n13. Perawatan Perbaikan Mesin / Engine\n14. Pengecatan Body\n15. Gambar Teknik\n16. Sistem Hydraulic Alat Berat\n17. Sistem Starter\n18. Sistem Electrical Body dan Panel Instrument\n19. Sistem Pengaman\n20. Sistem Bahan Bakar Bensin dan Diesel\n21. Sistem Kopling\n22. Sistem Differential / Gardan\n23. Sistem Kemudi\n24. Perawatan dan Perbaikan Kelistrikan\n25. Perawatan dan Perbaikan Sepeda Motor\n26. Perawatan dan Perbaikan Interior\n27. Diesel Engine Alat Berat\n28. Sistem Pemindah Tenaga (powertrain) dan Kerangka Bawah (undercarriage).\n29. Sistem Pengapian Konvensional dan Elektronik\n30. Sistem AC\n31. Sistem Control Electronik\n32. Sistem EMS\n33. Sistem Transmisi Manual dan Automatic\n34. Sistem Roda dan Poros Penggerak ( Axle Shaft )",
        "jadwal":{
            "10":{
                "senin":{
                    "1":{
                        "materi":"upacara",
                        "guru":"semua",
                        "ruang":"lapangan"
                    },
                    "2":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "3":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "4":{
                        "materi":"PP",
                        "guru":"Pak Luhur",
                        "ruang":"A.109"
                    },
                    "5":{
                        "materi":"PP",
                        "guru":"Pak Luhur",
                        "ruang":"A.109"
                    }
                },
                "selasa":{
                    "1":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "2":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "3":{
                        "materi":"PAI",
                        "guru":"Pak Marno",
                        "ruang":"B.103"
                    },
                    "4":{
                        "materi":"PAI",
                        "guru":"Pak Marno",
                        "ruang":"B.103"
                    },
                    "5":{
                        "materi":"BK",
                        "guru":"Mam Ayunda",
                        "ruang":"A.109"
                    },
                },
                "kamis":{
                    "1":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "2":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "3":{
                        "materi":"PKK",
                        "guru": "Mam Cantika",
                        "ruang": "C.113"
                    },
                    "4":{
                        "materi":"PKK",
                        "guru": "Mam Cantika",
                        "ruang": "C.113"
                    },
                    "5":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "6":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "7":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Aryo",
                        "ruang": "B.104"
                    },
                    "8":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Aryo",
                        "ruang": "B.104"
                    },
                    "9":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Aryo",
                        "ruang": "B.104"
                    },
                },
                "jumat":{
                    "1":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "2":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "3":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "4":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "5":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "6":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "7":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "8":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "9":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "10":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "11":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    }
                },
                "sabtu":{
                    "1":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "2":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "3":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "4":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "5":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "6":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "7":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "8":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "9":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "10":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "11":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    }
                },
            },
            "11":{
                "senin":{
                    "1":{
                        "materi":"upacara",
                        "guru":"-",
                        "ruang":"lapangan"
                    },
                    "2":{
                        "materi":"PP",
                        "guru":"Mam Wuri",
                        "ruang":"D.201"
                    },
                    "3":{
                        "materi":"PP",
                        "guru":"Mam Wuri",
                        "ruang":"D.201"
                    },
                    "4":{
                        "materi":"PP",
                        "guru":"Mam Wuri",
                        "ruang":"D.201"
                    },
                    "5":{
                        "materi":"B. Inggris",
                        "guru":"Mam Yus",
                        "ruang":"D.303"
                    },
                    "6":{
                        "materi":"B. Inggris",
                        "guru":"Mam Yus",
                        "ruang":"D.303"
                    }
                },
                "selasa":{
                    "1":{
                        "materi":"B. Indonesia",
                        "guru":"Pak Sobiron",
                        "ruang":"D.205"
                    },
                    "2":{
                        "materi":"B. Indonesia",
                        "guru":"Pak Sobiron",
                        "ruang":"D.205"
                    },
                    "3":{
                        "materi":"B. Indonesia",
                        "guru":"Pak Sobiron",
                        "ruang":"D.205"
                    },
                    "4":{
                        "materi":"Matematika",
                        "guru":"Mam Frida",
                        "ruang":"A.109"
                    },
                    "5":{
                        "materi":"Matematika",
                        "guru":"Mam Frida",
                        "ruang":"A.109"
                    },
                    "6":{
                        "materi":"Matematika",
                        "guru":"Mam Frida",
                        "ruang":"A.109"
                    },
                    "7":{
                        "materi":"PAI",
                        "guru":"Pak Marno",
                        "ruang":"B.103"
                    },
                    "8":{
                        "materi":"PAI",
                        "guru":"Pak Marno",
                        "ruang":"B.103"
                    }
                },
                "Rabu":{
                    "1":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    },
                    "2":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    },
                    "3":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    },
                    "4":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    },
                    "5":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    },
                    "6":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    },
                    "7":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    },
                    "8":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    },
                    "9":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    },
                    "10":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    }
                },
                "kamis":{
                    "2":{
                        "materi":"Project PKK",
                        "guru": "Pak Rofi'i",
                        "ruang": "C.112"
                    },
                    "3":{
                        "materi":"Project PKK",
                        "guru": "Pak Rofi'i",
                        "ruang": "C.112"
                    },
                    "4":{
                        "materi":"Project PKK",
                        "guru": "Pak Rofi'i",
                        "ruang": "C.112"
                    },
                    "5":{
                        "materi":"Matematika",
                        "guru": "Mam Frida",
                        "ruang": "A.109"
                    },
                    "6":{
                        "materi":"Matematika",
                        "guru": "Mam Frida",
                        "ruang": "A.109"
                    },
                    "7":{
                        "materi":"Sejarah",
                        "guru": "Pak Sugiono",
                        "ruang": "A.205"
                    },
                    "8":{
                        "materi":"Sejarah",
                        "guru": "Pak Sugiono",
                        "ruang": "A.205"
                    },
                    "9":{
                        "materi":"Sejarah",
                        "guru": "Pak Sugiono",
                        "ruang": "A.205"
                    }
                },
                "jumat":{
                    "1":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    },
                    "2":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    },
                    "3":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    },
                    "4":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    },
                    "5":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    },
                    "6":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    },
                    "8":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    },
                    "9":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    },
                    "10":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    },
                    "11":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    }
                },
                "sabtu":{
                    "1":{
                        "materi":"BK",
                        "guru": "Mam Andhini",
                        "ruang": "C. 205"
                    },
                    "2":{
                        "materi":"PKK",
                        "guru": "Mam Cantika",
                        "ruang": "D.102"
                    },
                    "3":{
                        "materi":"PKK",
                        "guru": "Mam Cantika",
                        "ruang": "D.102"
                    },
                    "4":{
                        "materi":"PKK",
                        "guru": "Mam Cantika",
                        "ruang": "D.102"
                    },
                    "5":{
                        "materi":"Olahraga",
                        "guru": "Pak Suparno",
                        "ruang": "Lapangan"
                    },
                    "6":{
                        "materi":"Olahraga",
                        "guru": "Pak Suparno",
                        "ruang": "Lapangan"
                    },
                    "7":{
                        "materi":"Olahraga",
                        "guru": "Pak Suparno",
                        "ruang": "Lapangan"
                    },
                    "8":{
                        "materi":"B. Inggris",
                        "guru": "Mam Yus",
                        "ruang": "D.303"
                    },
                    "9":{
                        "materi":"B. Inggris",
                        "guru": "Mam Yus",
                        "ruang": "D.303"
                    },
                    "10":{
                        "materi":"B. Inggris",
                        "guru": "Mam Yus",
                        "ruang": "D.303"
                    }
                },

            },
            "12":{
                "senin":{
                    "1":{
                        "materi":"upacara",
                        "guru":"-",
                        "ruang":"lapangan"
                    },
                    "2":{
                        "materi":"PAI",
                        "guru":"Pak Sueb",
                        "ruang":"C.115"
                    },
                    "3":{
                        "materi":"PAI",
                        "guru":"Pak Sueb",
                        "ruang":"C.115"
                    },
                    "4":{
                        "materi":"Matematika",
                        "guru":"Pak Frida",
                        "ruang":"D.104"
                    },
                    "5":{
                        "materi":"Matematika",
                        "guru":"Pak Frida",
                        "ruang":"D.104"
                    },
                    "6":{
                        "materi":"Matematika",
                        "guru":"Pak Frida",
                        "ruang":"D.104"
                    },
                    "7":{
                        "materi":"Matematika",
                        "guru":"Pak Frida",
                        "ruang":"D.104"
                    }
                },
                "selasa":{
                    "3":{
                        "materi":"Olahraga",
                        "guru":"Pak Sumono",
                        "ruang":"Lapangan"
                    },
                    "4":{
                        "materi":"Olahraga",
                        "guru":"Pak Sumono",
                        "ruang":"Lapangan"
                    },
                    "5":{
                        "materi":"PP",
                        "guru":"Pak Erwin",
                        "ruang":"B.206"
                    },
                    "6":{
                        "materi":"PP",
                        "guru":"Pak Erwin",
                        "ruang":"B.206"
                    },
                    "7":{
                        "materi":"PKK",
                        "guru":"Mam Ine",
                        "ruang":"D.101"
                    },
                    "8":{
                        "materi":"PKK",
                        "guru":"Mam Ine",
                        "ruang":"D.101"
                    },
                    "9":{
                        "materi":"B. Inggris",
                        "guru":"Miss Alrina",
                        "ruang":"D.204"
                    },
                    "10":{
                        "materi":"B. Inggris",
                        "guru":"Miss Alrina",
                        "ruang":"D.204"
                    }
                },
                "rabu":{
                    "1":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "2":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "3":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "4":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "5":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "6":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "7":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "8":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "9":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "10":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    }
                },
                "kamis":{
                    "1":{
                        "materi":"BK",
                        "guru": "Pak Sugiarto",
                        "ruang": "A.108"
                    },
                    "2":{
                        "materi":"BK",
                        "guru": "Pak Sugiarto",
                        "ruang": "A.108"
                    },
                    "3":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Hartono",
                        "ruang": "A.108"
                    },
                    "4":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Hartono",
                        "ruang": "A.108"
                    },
                    "5":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Hartono",
                        "ruang": "A.108"
                    },
                    "6":{
                        "materi":"B. Inggris",
                        "guru": "Miss Alrina",
                        "ruang": "D.204"
                    },
                },
                "sabtu":{
                    "1":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "2":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "3":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "4":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "5":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "6":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "7":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "8":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "9":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "10":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    }
                },
            },
        }
    },
    "TM":{
        "kerja": "1. PT. Toyota Manufacturing Indonesia\n2. PT. Astra Daihatsu Motor\n3. PT. Dua Kelinci\n4. PT. GS Battery\n5. CV. New Ratna Motor ( Nasmoco )\n6. PT. Astra Honda Motor\n7. PT. Pamapersada Nusantara\n8. PT. Jiaec\n9. PT. United Tractors\n10. CV. Surya Indah Motor",
        "profil":"Teknik Mesin adalah suatu disiplin ilmu teknik yang menggabungkan fisika teknik dan prinsip-prinsip matematika dengan ilmu material (bahan) untuk mendesain, menganalisa, dan membuat serta mempertahankan sistem mekanis. Teknik Mesin merupakan salah satu bidang ilmu teknik yang paling tua di dunia. Beberapa bidang ilmu yang menjadi inti dari Teknik Mesin adalah mekanika, dinamika, termodinamika, ilmu material, analisa struktur, dan kelistrikan. Di samping itu, ada sejumlah alat bantu (tool) yang dipergunakan di bidang Teknik Mesin ini, antara lain CAD (computer-aided design), CAM (computer-aided manufacturing). Jurusan Teknik Mesin SMK Tunas Harapan Pati juga menerapkan pembelajaran TEFA, dimana sekolah menerima Job / orderan dari luar yang nantinya akan dikerjakan oleh siswa, dengan tujuan siswa mendapat pengalaman langsung dalam mengerjakan job dari industri.",
        "materi":"1. Pekerjaan Dasar Teknik Mesin\n2. Ilmu Bahan\n3. Kewirausahaan\n4. Pemesinan Gerinda\n5. Teknik Gambar Produksi\n6. CAD/CAM\n7. Gambar Teknik\n8. Pengelasann Dasar\n9. Pemesinan Bubut\n10. Perancangan Dasar Teknik Mesin\n11. Pemesinan NC/CNC Turning\n12. Mekanika Teknik\n13. Bisnis Manufaktur\n14. Pemesinan Frais\n15. Teknik Gambar Kontruksi\n 16. Pemesinan NC/CNC Milling",
        "jadwal":{
            "10":{
                "senin":{
                    "1":{
                        "materi":"upacara",
                        "guru":"semua",
                        "ruang":"lapangan"
                    },
                    "2":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "3":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "4":{
                        "materi":"PP",
                        "guru":"Pak Luhur",
                        "ruang":"A.109"
                    },
                    "5":{
                        "materi":"PP",
                        "guru":"Pak Luhur",
                        "ruang":"A.109"
                    }
                },
                "selasa":{
                    "1":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "2":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "3":{
                        "materi":"PAI",
                        "guru":"Pak Marno",
                        "ruang":"B.103"
                    },
                    "4":{
                        "materi":"PAI",
                        "guru":"Pak Marno",
                        "ruang":"B.103"
                    },
                    "5":{
                        "materi":"BK",
                        "guru":"Mam Ayunda",
                        "ruang":"A.109"
                    },
                },
                "kamis":{
                    "1":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "2":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "3":{
                        "materi":"PKK",
                        "guru": "Mam Cantika",
                        "ruang": "C.113"
                    },
                    "4":{
                        "materi":"PKK",
                        "guru": "Mam Cantika",
                        "ruang": "C.113"
                    },
                    "5":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "6":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "7":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Aryo",
                        "ruang": "B.104"
                    },
                    "8":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Aryo",
                        "ruang": "B.104"
                    },
                    "9":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Aryo",
                        "ruang": "B.104"
                    },
                },
                "jumat":{
                    "1":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "2":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "3":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "4":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "5":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "6":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "7":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "8":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "9":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "10":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "11":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    }
                },
                "sabtu":{
                    "1":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "2":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "3":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "4":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "5":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "6":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "7":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "8":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "9":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "10":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "11":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    }
                },
            },
            "11":{
                "senin":{
                    "1":{
                        "materi":"upacara",
                        "guru":"-",
                        "ruang":"lapangan"
                    },
                    "2":{
                        "materi":"PP",
                        "guru":"Mam Wuri",
                        "ruang":"D.201"
                    },
                    "3":{
                        "materi":"PP",
                        "guru":"Mam Wuri",
                        "ruang":"D.201"
                    },
                    "4":{
                        "materi":"PP",
                        "guru":"Mam Wuri",
                        "ruang":"D.201"
                    },
                    "5":{
                        "materi":"B. Inggris",
                        "guru":"Mam Yus",
                        "ruang":"D.303"
                    },
                    "6":{
                        "materi":"B. Inggris",
                        "guru":"Mam Yus",
                        "ruang":"D.303"
                    }
                },
                "selasa":{
                    "1":{
                        "materi":"B. Indonesia",
                        "guru":"Pak Sobiron",
                        "ruang":"D.205"
                    },
                    "2":{
                        "materi":"B. Indonesia",
                        "guru":"Pak Sobiron",
                        "ruang":"D.205"
                    },
                    "3":{
                        "materi":"B. Indonesia",
                        "guru":"Pak Sobiron",
                        "ruang":"D.205"
                    },
                    "4":{
                        "materi":"Matematika",
                        "guru":"Mam Frida",
                        "ruang":"A.109"
                    },
                    "5":{
                        "materi":"Matematika",
                        "guru":"Mam Frida",
                        "ruang":"A.109"
                    },
                    "6":{
                        "materi":"Matematika",
                        "guru":"Mam Frida",
                        "ruang":"A.109"
                    },
                    "7":{
                        "materi":"PAI",
                        "guru":"Pak Marno",
                        "ruang":"B.103"
                    },
                    "8":{
                        "materi":"PAI",
                        "guru":"Pak Marno",
                        "ruang":"B.103"
                    }
                },
                "Rabu":{
                    "1":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    },
                    "2":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    },
                    "3":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    },
                    "4":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    },
                    "5":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    },
                    "6":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    },
                    "7":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    },
                    "8":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    },
                    "9":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    },
                    "10":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    }
                },
                "kamis":{
                    "2":{
                        "materi":"Project PKK",
                        "guru": "Pak Rofi'i",
                        "ruang": "C.112"
                    },
                    "3":{
                        "materi":"Project PKK",
                        "guru": "Pak Rofi'i",
                        "ruang": "C.112"
                    },
                    "4":{
                        "materi":"Project PKK",
                        "guru": "Pak Rofi'i",
                        "ruang": "C.112"
                    },
                    "5":{
                        "materi":"Matematika",
                        "guru": "Mam Frida",
                        "ruang": "A.109"
                    },
                    "6":{
                        "materi":"Matematika",
                        "guru": "Mam Frida",
                        "ruang": "A.109"
                    },
                    "7":{
                        "materi":"Sejarah",
                        "guru": "Pak Sugiono",
                        "ruang": "A.205"
                    },
                    "8":{
                        "materi":"Sejarah",
                        "guru": "Pak Sugiono",
                        "ruang": "A.205"
                    },
                    "9":{
                        "materi":"Sejarah",
                        "guru": "Pak Sugiono",
                        "ruang": "A.205"
                    }
                },
                "jumat":{
                    "1":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    },
                    "2":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    },
                    "3":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    },
                    "4":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    },
                    "5":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    },
                    "6":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    },
                    "8":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    },
                    "9":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    },
                    "10":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    },
                    "11":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    }
                },
                "sabtu":{
                    "1":{
                        "materi":"BK",
                        "guru": "Mam Andhini",
                        "ruang": "C. 205"
                    },
                    "2":{
                        "materi":"PKK",
                        "guru": "Mam Cantika",
                        "ruang": "D.102"
                    },
                    "3":{
                        "materi":"PKK",
                        "guru": "Mam Cantika",
                        "ruang": "D.102"
                    },
                    "4":{
                        "materi":"PKK",
                        "guru": "Mam Cantika",
                        "ruang": "D.102"
                    },
                    "5":{
                        "materi":"Olahraga",
                        "guru": "Pak Suparno",
                        "ruang": "Lapangan"
                    },
                    "6":{
                        "materi":"Olahraga",
                        "guru": "Pak Suparno",
                        "ruang": "Lapangan"
                    },
                    "7":{
                        "materi":"Olahraga",
                        "guru": "Pak Suparno",
                        "ruang": "Lapangan"
                    },
                    "8":{
                        "materi":"B. Inggris",
                        "guru": "Mam Yus",
                        "ruang": "D.303"
                    },
                    "9":{
                        "materi":"B. Inggris",
                        "guru": "Mam Yus",
                        "ruang": "D.303"
                    },
                    "10":{
                        "materi":"B. Inggris",
                        "guru": "Mam Yus",
                        "ruang": "D.303"
                    }
                },

            },
            "12":{
                "senin":{
                    "1":{
                        "materi":"upacara",
                        "guru":"-",
                        "ruang":"lapangan"
                    },
                    "2":{
                        "materi":"PAI",
                        "guru":"Pak Sueb",
                        "ruang":"C.115"
                    },
                    "3":{
                        "materi":"PAI",
                        "guru":"Pak Sueb",
                        "ruang":"C.115"
                    },
                    "4":{
                        "materi":"Matematika",
                        "guru":"Pak Frida",
                        "ruang":"D.104"
                    },
                    "5":{
                        "materi":"Matematika",
                        "guru":"Pak Frida",
                        "ruang":"D.104"
                    },
                    "6":{
                        "materi":"Matematika",
                        "guru":"Pak Frida",
                        "ruang":"D.104"
                    },
                    "7":{
                        "materi":"Matematika",
                        "guru":"Pak Frida",
                        "ruang":"D.104"
                    }
                },
                "selasa":{
                    "3":{
                        "materi":"Olahraga",
                        "guru":"Pak Sumono",
                        "ruang":"Lapangan"
                    },
                    "4":{
                        "materi":"Olahraga",
                        "guru":"Pak Sumono",
                        "ruang":"Lapangan"
                    },
                    "5":{
                        "materi":"PP",
                        "guru":"Pak Erwin",
                        "ruang":"B.206"
                    },
                    "6":{
                        "materi":"PP",
                        "guru":"Pak Erwin",
                        "ruang":"B.206"
                    },
                    "7":{
                        "materi":"PKK",
                        "guru":"Mam Ine",
                        "ruang":"D.101"
                    },
                    "8":{
                        "materi":"PKK",
                        "guru":"Mam Ine",
                        "ruang":"D.101"
                    },
                    "9":{
                        "materi":"B. Inggris",
                        "guru":"Miss Alrina",
                        "ruang":"D.204"
                    },
                    "10":{
                        "materi":"B. Inggris",
                        "guru":"Miss Alrina",
                        "ruang":"D.204"
                    }
                },
                "rabu":{
                    "1":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "2":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "3":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "4":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "5":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "6":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "7":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "8":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "9":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "10":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    }
                },
                "kamis":{
                    "1":{
                        "materi":"BK",
                        "guru": "Pak Sugiarto",
                        "ruang": "A.108"
                    },
                    "2":{
                        "materi":"BK",
                        "guru": "Pak Sugiarto",
                        "ruang": "A.108"
                    },
                    "3":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Hartono",
                        "ruang": "A.108"
                    },
                    "4":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Hartono",
                        "ruang": "A.108"
                    },
                    "5":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Hartono",
                        "ruang": "A.108"
                    },
                    "6":{
                        "materi":"B. Inggris",
                        "guru": "Miss Alrina",
                        "ruang": "D.204"
                    },
                },
                "sabtu":{
                    "1":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "2":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "3":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "4":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "5":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "6":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "7":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "8":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "9":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    },
                    "10":{
                        "materi":"OTO A/B",
                        "guru": "Pak Andrai/Pak Yosi",
                        "ruang": "Bengkel Otomotif"
                    }
                },
            },
        }
    },
    "LAS":{
        "kerja": "1. PT. Toyota Manufacturing Indonesia\n2. PT. Astra Daihatsu Motor\n3. PT. Dua Kelinci\n4. PT.United Tractors Pandu Engineering\n5. PT. Pura Barutama\n6. PT. Astra Honda Motor\n7. PT. Pamapersada Nusantara\n8. PT. Jiaec\n9. PT.United Tractors Pandu Engineering\n10. Karoseri Laksana\n11. PT.Dian Pandu Pratama",
        "profil":"Program Keahlian Teknik Pengelasan Dan Fabrikasi logam SMK Tunas Harapan Pati merupakan salah satu Program keahlian yang Membekali peserta didik dengan keterampilan, pengetahuan dan sikap agar kompeten mengembangkan kemampuan dan kemandirian dalam berwirausaha dibidang pengelasan, menyiapkan peserta didik agar memiliki pribadi yang jujur, sopan dan berwibawa, Menyiapkan peserta didik yang terampil dibidang pengelasan sesuai dengan kebutuhan industri, dan menjalin hubungan yang sinergi dengan dunia usaha atau Dunia Industri (DU/DI). Selain itu lulusan Program keahlian Teknik pengelasan dan fabrikasi logam dibekali sertifikat kompetensi yang diuji oleh pihak luar untuk memerikan pengukuhan kompeten dibidangnya agar dapat memenuhi kebutuhan industri dibidang pengelasan.",
        "materi":"1. Proses bisnis bidang pengelasan dan fabrikasi logam\n2. Teknik dasar pada bidang teknologi pengelasan dan fabrikasi logam\n3. Penggunaan perkakas bengkel\n4. Pengelasan Shielded Metal Arc Welding (SMAW)\n5. Pengelasan Gas Tungsten Arc Welding (GTAW)\n6. Perkembangan teknologi di bidang pengelasan dan fabrikasi logam\n7. Keselamatan dan Kesehatan Kerja Lingkungan Hidup (K3LH) dan budaya kerja industri\n8. Pengelasan SMAW dasar\n9. Pengelasan Gas Metal Arc Welding (GMAW)\n10. Mutu Pengelasan\n11. Profesi dan kewirausahaan di bidang pengelasan dan fabrikasi logam\n12. Gambar teknik\n13. Pengelasan Oxy Acetylene Welding (OAW)\n14. Pengelasan Flux Core Arc Welding (FCAW)\n15. Teknik Fabrikasi Logam",
        "jadwal":{
            "10":{
                "senin":{
                    "1":{
                        "materi":"upacara",
                        "guru":"semua",
                        "ruang":"lapangan"
                    },
                    "2":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "3":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "4":{
                        "materi":"PP",
                        "guru":"Pak Luhur",
                        "ruang":"A.109"
                    },
                    "5":{
                        "materi":"PP",
                        "guru":"Pak Luhur",
                        "ruang":"A.109"
                    }
                },
                "selasa":{
                    "1":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "2":{
                        "materi":"B. Inggris",
                        "guru":"Mam Kris",
                        "ruang":"D.204"
                    },
                    "3":{
                        "materi":"PAI",
                        "guru":"Pak Marno",
                        "ruang":"B.103"
                    },
                    "4":{
                        "materi":"PAI",
                        "guru":"Pak Marno",
                        "ruang":"B.103"
                    },
                    "5":{
                        "materi":"BK",
                        "guru":"Mam Ayunda",
                        "ruang":"A.109"
                    },
                },
                "kamis":{
                    "1":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "2":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "3":{
                        "materi":"PKK",
                        "guru": "Mam Cantika",
                        "ruang": "C.113"
                    },
                    "4":{
                        "materi":"PKK",
                        "guru": "Mam Cantika",
                        "ruang": "C.113"
                    },
                    "5":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "6":{
                        "materi":"Matematika",
                        "guru": "Mam Diah",
                        "ruang": "D.201"
                    },
                    "7":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Aryo",
                        "ruang": "B.104"
                    },
                    "8":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Aryo",
                        "ruang": "B.104"
                    },
                    "9":{
                        "materi":"B. Indonesia",
                        "guru": "Pak Aryo",
                        "ruang": "B.104"
                    },
                },
                "jumat":{
                    "1":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "2":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "3":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "4":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "5":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "6":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "7":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "8":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "9":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "10":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    },
                    "11":{
                        "materi":"PIC",
                        "guru": "Pak Andi",
                        "ruang": "Perakitan"
                    }
                },
                "sabtu":{
                    "1":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "2":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "3":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "4":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "5":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "6":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "7":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "8":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "9":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "10":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    },
                    "11":{
                        "materi":"PCC",
                        "guru": "Pak Abdyll",
                        "ruang": "WAN"
                    }
                },
            },
            "11":{
                "senin":{
                    "1":{
                        "materi":"upacara",
                        "guru":"-",
                        "ruang":"lapangan"
                    },
                    "2":{
                        "materi":"PP",
                        "guru":"Mam Wuri",
                        "ruang":"D.201"
                    },
                    "3":{
                        "materi":"PP",
                        "guru":"Mam Wuri",
                        "ruang":"D.201"
                    },
                    "4":{
                        "materi":"PP",
                        "guru":"Mam Wuri",
                        "ruang":"D.201"
                    },
                    "5":{
                        "materi":"B. Inggris",
                        "guru":"Mam Yus",
                        "ruang":"D.303"
                    },
                    "6":{
                        "materi":"B. Inggris",
                        "guru":"Mam Yus",
                        "ruang":"D.303"
                    }
                },
                "selasa":{
                    "1":{
                        "materi":"B. Indonesia",
                        "guru":"Pak Sobiron",
                        "ruang":"D.205"
                    },
                    "2":{
                        "materi":"B. Indonesia",
                        "guru":"Pak Sobiron",
                        "ruang":"D.205"
                    },
                    "3":{
                        "materi":"B. Indonesia",
                        "guru":"Pak Sobiron",
                        "ruang":"D.205"
                    },
                    "4":{
                        "materi":"Matematika",
                        "guru":"Mam Frida",
                        "ruang":"A.109"
                    },
                    "5":{
                        "materi":"Matematika",
                        "guru":"Mam Frida",
                        "ruang":"A.109"
                    },
                    "6":{
                        "materi":"Matematika",
                        "guru":"Mam Frida",
                        "ruang":"A.109"
                    },
                    "7":{
                        "materi":"PAI",
                        "guru":"Pak Marno",
                        "ruang":"B.103"
                    },
                    "8":{
                        "materi":"PAI",
                        "guru":"Pak Marno",
                        "ruang":"B.103"
                    }
                },
                "Rabu":{
                    "1":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    },
                    "2":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    },
                    "3":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    },
                    "4":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    },
                    "5":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    },
                    "6":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    },
                    "7":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    },
                    "8":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    },
                    "9":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    },
                    "10":{
                        "materi":"OTO A",
                        "guru":"Pak Nurivan",
                        "ruang":"Lab Engine"
                    }
                },
                "kamis":{
                    "2":{
                        "materi":"Project PKK",
                        "guru": "Pak Rofi'i",
                        "ruang": "C.112"
                    },
                    "3":{
                        "materi":"Project PKK",
                        "guru": "Pak Rofi'i",
                        "ruang": "C.112"
                    },
                    "4":{
                        "materi":"Project PKK",
                        "guru": "Pak Rofi'i",
                        "ruang": "C.112"
                    },
                    "5":{
                        "materi":"Matematika",
                        "guru": "Mam Frida",
                        "ruang": "A.109"
                    },
                    "6":{
                        "materi":"Matematika",
                        "guru": "Mam Frida",
                        "ruang": "A.109"
                    },
                    "7":{
                        "materi":"Sejarah",
                        "guru": "Pak Sugiono",
                        "ruang": "A.205"
                    },
                    "8":{
                        "materi":"Sejarah",
                        "guru": "Pak Sugiono",
                        "ruang": "A.205"
                    },
                    "9":{
                        "materi":"Sejarah",
                        "guru": "Pak Sugiono",
                        "ruang": "A.205"
                    }
                },
                "jumat":{
                    "1":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    },
                    "2":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    },
                    "3":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    },
                    "4":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    },
                    "5":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    },
                    "6":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    },
                    "8":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    },
                    "9":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    },
                    "10":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    },
                    "11":{
                        "materi":"OTO B",
                        "guru": "Pak Made",
                        "ruang": "LAB Electrical 2"
                    }
                },
                "sabtu":{
                    "1":{
                        "materi":"BK",
                        "guru": "Mam Andhini",
                        "ruang": "C. 205"
                    },
                    "2":{
                        "materi":"PKK",
                        "guru": "Mam Cantika",
                        "ruang": "D.102"
                    },
                    "3":{
                        "materi":"PKK",
                        "guru": "Mam Cantika",
                        "ruang": "D.102"
                    },
                    "4":{
                        "materi":"PKK",
                        "guru": "Mam Cantika",
                        "ruang": "D.102"
                    },
                    "5":{
                        "materi":"Olahraga",
                        "guru": "Pak Suparno",
                        "ruang": "Lapangan"
                    },
                    "6":{
                        "materi":"Olahraga",
                        "guru": "Pak Suparno",
                        "ruang": "Lapangan"
                    },
                    "7":{
                        "materi":"Olahraga",
                        "guru": "Pak Suparno",
                        "ruang": "Lapangan"
                    },
                    "8":{
                        "materi":"B. Inggris",
                        "guru": "Mam Yus",
                        "ruang": "D.303"
                    },
                    "9":{
                        "materi":"B. Inggris",
                        "guru": "Mam Yus",
                        "ruang": "D.303"
                    },
                    "10":{
                        "materi":"B. Inggris",
                        "guru": "Mam Yus",
                        "ruang": "D.303"
                    }
                },

            },
            "12":{
                "senin":{
                    "1":{
                        "materi":"upacara",
                        "guru":"-",
                        "ruang":"lapangan"
                    },
                    "2":{
                        "materi":"TFL",
                        "guru":"Pak Furqon",
                        "ruang":"AREA XI GMAW"
                    },
                    "3":{
                        "materi":"TFL",
                        "guru":"Pak Furqon",
                        "ruang":"AREA XI GMAW"
                    },
                    "4":{
                        "materi":"TFL",
                        "guru":"Pak Furqon",
                        "ruang":"AREA XI GMAW"
                    },
                    "5":{
                        "materi":"TFL",
                        "guru":"Pak Furqon",
                        "ruang":"AREA XI GMAW"
                    },
                    "6":{
                        "materi":"GTAW",
                        "guru":"Pak Baud",
                        "ruang":"AREA XII GMAW"
                    },
                    "7":{
                        "materi":"GTAW",
                        "guru":"Pak Baud",
                        "ruang":"AREA XII GMAW"
                    },
                    "8":{
                        "materi":"GTAW",
                        "guru":"Pak Baud",
                        "ruang":"AREA XII GMAW"
                    },
                    "9":{
                        "materi":"GTAW",
                        "guru":"Pak Baud",
                        "ruang":"AREA XII GMAW"
                    },
                    "10":{
                        "materi":"GTAW",
                        "guru":"Pak Baud",
                        "ruang":"AREA XII GMAW"
                    }
                },
                "selasa":{
                    "1":{
                        "materi":"PKK",
                        "guru":"Mam Chryse",
                        "ruang":"BASIC SMAW"
                    },
                    "2":{
                        "materi":"PKK",
                        "guru":"Mam Chryse",
                        "ruang":"BASIC SMAW"
                    },
                    "3":{
                        "materi":"PKK",
                        "guru":"Mam Chryse",
                        "ruang":"BASIC SMAW"
                    },
                    "4":{
                        "materi":"PKK",
                        "guru":"Mam Chryse",
                        "ruang":"BASIC SMAW"
                    },
                    "5":{
                        "materi":"GMAW",
                        "guru":"Pak Yanto",
                        "ruang":"AREA XII GMAW"
                    },
                    "6":{
                        "materi":"GMAW",
                        "guru":"Pak Yanto",
                        "ruang":"AREA XII GMAW"
                    },
                    "7":{
                        "materi":"GMAW",
                        "guru":"Pak Yanto",
                        "ruang":"AREA XII GMAW"
                    },
                    "8":{
                        "materi":"GMAW",
                        "guru":"Pak Yanto",
                        "ruang":"AREA XII GMAW"
                    },
                    "9":{
                        "materi":"GMAW",
                        "guru":"Pak Yanto",
                        "ruang":"AREA XII GMAW"
                    },
                    "10":{
                        "materi":"GMAW",
                        "guru":"Pak Yanto",
                        "ruang":"AREA XII GMAW"
                    }
                },
                "rabu":{
                    "5":{
                        "materi":"B. Inggris",
                        "guru": "Mam Yusnita",
                        "ruang": "D.303"
                    },
                    "6":{
                        "materi":"B. Inggris",
                        "guru": "Mam Yusnita",
                        "ruang": "D.303"
                    },
                    "7":{
                        "materi":"PP",
                        "guru": "Mam Wuri",
                        "ruang": "A.111"
                    },
                    "8":{
                        "materi":"PP",
                        "guru": "Mam Wuri",
                        "ruang": "A.111"
                    },
                    "9":{
                        "materi":"PAI",
                        "guru": "Pak Slamet",
                        "ruang": "C.114"
                    },
                    "10":{
                        "materi":"PAI",
                        "guru": "Pak Slamet",
                        "ruang": "C.114"
                    }
                },
                "kamis":{
                    "1":{
                        "materi":"PKK",
                        "guru": "Mam Cantika",
                        "ruang": "C.113"
                    },
                    "2":{
                        "materi":"PKK",
                        "guru": "Mam Cantika",
                        "ruang": "C.113"
                    },
                    "3":{
                        "materi":"BK",
                        "guru": "Mam Ayudhia",
                        "ruang": "D.203"
                    },
                    "4":{
                        "materi":"BK",
                        "guru": "Mam Ayudhia",
                        "ruang": "D.203"
                    },
                    "5":{
                        "materi":"Matematika",
                        "guru": "Pak Heri",
                        "ruang": "D.206"
                    },
                    "6":{
                        "materi":"Matematika",
                        "guru": "Miss Heri",
                        "ruang": "D.206"
                    },
                    "7":{
                        "materi":"B. Indonesia",
                        "guru": "Mam Dhita",
                        "ruang": "B.204"
                    },
                    "8":{
                        "materi":"B. Indonesia",
                        "guru": "Mam Dhita",
                        "ruang": "B.204"
                    },
                    "9":{
                        "materi":"B. Indonesia",
                        "guru": "Mam Dhita",
                        "ruang": "B.204"
                    },
                },
                "jumat":{
                    "3":{
                        "materi":"B. Inggris",
                        "guru": "Mam Yusnita",
                        "ruang": "D.303"
                    },
                    "4":{
                        "materi":"B. Inggris",
                        "guru": "Mam Yusnita",
                        "ruang": "D.303"
                    },
                    "5":{
                        "materi":"GT",
                        "guru": "Pak Furqon",
                        "ruang": "D.306"
                    },
                    "6":{
                        "materi":"GT",
                        "guru": "Pak Furqon",
                        "ruang": "D.306"
                    },
                    "8":{
                        "materi":"Matematika",
                        "guru": "Pak Heri",
                        "ruang": "D.206"
                    },
                    "9":{
                        "materi":"Matematika",
                        "guru": "Pak Heri",
                        "ruang": "D.206"
                    }
                },
                "sabtu":{
                    "1":{
                        "materi":"SMAW",
                        "guru": "Pak Baud",
                        "ruang": "AREA XII GMAW"
                    },
                    "2":{
                        "materi":"SMAW",
                        "guru": "Pak Baud",
                        "ruang": "AREA XII GMAW"
                    },
                    "3":{
                        "materi":"SMAW",
                        "guru": "Pak Baud",
                        "ruang": "AREA XII GMAW"
                    },
                    "4":{
                        "materi":"SMAW",
                        "guru": "Pak Baud",
                        "ruang": "AREA XII GMAW"
                    },
                    "5":{
                        "materi":"SMAW",
                        "guru": "Pak Baud",
                        "ruang": "AREA XII GMAW"
                    },
                    "6":{
                        "materi":"SMAW",
                        "guru": "Pak Baud",
                        "ruang": "AREA XII GMAW"
                    },
                    "7":{
                        "materi":"FCAW",
                        "guru": "Pak Yanto",
                        "ruang": "AREA XII SMAW"
                    },
                    "8":{
                        "materi":"FCAW",
                        "guru": "Pak Yanto",
                        "ruang": "AREA XII SMAW"
                    },
                    "9":{
                        "materi":"FCAW",
                        "guru": "Pak Yanto",
                        "ruang": "AREA XII SMAW"
                    },
                    "10":{
                        "materi":"FCAW",
                        "guru": "Pak Yanto",
                        "ruang": "AREA XII SMAW"
                    },
                    "11":{
                        "materi":"FCAW",
                        "guru": "Pak Yanto",
                        "ruang": "AREA XII SMAW"
                    },
                    "12":{
                        "materi":"FCAW",
                        "guru": "Pak Yanto",
                        "ruang": "AREA XII SMAW"
                    },
                },
            },
        }
    },

}

class ActionGetGuru(Action):
    def name(self) -> Text:
        return "action_get_guru"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            jurusan = tracker.get_slot("jurusan")
            kelas = tracker.get_slot("kelas")
            materi = tracker.get_slot("materi")
            guru = tracker.get_slot("key_guru")
            
            if guru and jurusan and kelas and materi:
                data = guru_dictionary.get(guru.lower(),{}).get(jurusan.upper(),{}).get(materi.lower(),{}).get(str(kelas))
                if data:
                    dispatcher.utter_message(text=f"{guru} {materi} kelas {kelas} {jurusan} adalah {data}")
                else:
                    dispatcher.utter_message(text=f"Di Kelas itu tidak ada pelajaran {materi} kak")
     
            elif not materi:
                dispatcher.utter_message(text=f"tolong masukkan materi yang diajar guru tersebut ya kak :)")
            else:
                dispatcher.utter_message(text=f"Tolong masukkan lagi materi yang diajar kelas dan jurusannya juga ya kak :)")
            return []
            

class ActionGetJadwal(Action):
    def name(self) -> Text:
        return "action_get_jadwal"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        hari = tracker.get_slot("hari")
        jurusan = tracker.get_slot("jurusan")
        kelas = tracker.get_slot("kelas")
        key_jadwal = tracker.get_slot("key_jadwal")

        set_locale_to_indonesian()
        hari_ini = datetime.now().strftime("%A").lower()

        if key_jadwal and hari and jurusan and kelas:
            jadwal_kelas = data_dictionary.get(jurusan.upper(),{}).get(key_jadwal.lower(),{}).get(str(kelas),{}).get(hari.lower(),{})
            if jadwal_kelas:
                pesan = f"DITA kasih tau ya kak jadwal hari {hari} kelas {kelas} jurusan {jurusan} yaitu:\n"
                for jam, info in jadwal_kelas.items():
                    pesan += f"Jam ke-{jam}: materi {info['materi']} dengan guru {info['guru']} di ruang {info['ruang']}\n"
                dispatcher.utter_message(pesan)
            else:
                dispatcher.utter_message("Kelas ini sedang libur kak :)")
        elif key_jadwal and jurusan and kelas:
            jadwal_hari_ini = data_dictionary.get(jurusan.upper()).get("jadwal",{}).get(str(kelas),{}).get(hari_ini.lower(),{})

            if jadwal_hari_ini:
                message=f"DITA kasih tau ya kak jadwal hari ini kelas {kelas} jurusan {jurusan} yaitu:\n"
                for jam, info in jadwal_hari_ini.items():
                    materi = info.get('materi','')
                    guru = info.get('guru', '')
                    ruang = info.get('ruang', '')
                    message += f"Jam {jam}: materi {materi},guru {guru},ruang {ruang}\n"
                dispatcher.utter_message(text=message)
            else:
                dispatcher.utter_message(text="kelas tersebut sedang libur kak :)")
        else:
            dispatcher.utter_message(text="tolong masukkan kelas dan jurusannya ya kak :)")
        return []

class ActionGetProfil(Action):
    def name(self) -> Text:
        return "action_get_profil"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            jurusan = tracker.get_slot("jurusan")
            key_profil = tracker.get_slot("key_profil")

            if key_profil and jurusan:
                profil = data_dictionary.get(jurusan.upper(),{}).get(key_profil.lower(),{})
                dispatcher.utter_message(text="Baik kak, tunggu sebentar ya...")
                dispatcher.utter_message(text=f"{profil}")
            elif key_profil:
                dispatcher.utter_message(text="Tolong masukkan jurusannya ya kak :)")
            else:
                dispatcher.utter_message(text="Maaf kak, DITA masih tahap pengembangan jadi belum bisa tau profil semua jurusan dan tolong pastikan kak penggunaan singkatan dengan huruf besar")

            return []


class ActionGetKerja(Action):
    def name(self) -> Text:
        return "action_get_kerja"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            jurusan = tracker.get_slot("jurusan")
            key_kerja = tracker.get_slot("key_kerja")

            if key_kerja and jurusan:
                kerja = data_dictionary.get(jurusan.upper(),{}).get(key_kerja.lower(),{})
                dispatcher.utter_message(text="Baik kak, tunggu sebentar ya...")
                dispatcher.utter_message(text=f"{kerja}")
            else:
                dispatcher.utter_message(text=f"Tolong masukkan jurusannya ya kak :)")
            return []


class ActionGetMapel(Action):
    def name(self) -> Text:
        return "action_get_mapel"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            jurusan = tracker.get_slot("jurusan")
            key_mapel = tracker.get_slot("key_mapel")

            if key_mapel and jurusan:
                materi = data_dictionary.get(jurusan.upper(),{}).get(key_mapel.lower(),{})
                dispatcher.utter_message(text="Baik kak, tunggu sebentar ya...")
                dispatcher.utter_message(text=f"{materi}")
            else:
                dispatcher.utter_message(text=f"Tolong masukkan jurusannya ya kak :)")
            return []

class ActionGetProfilSekolah(Action):
    def name(self) -> Text:
        return "action_profil_sekolah"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            profil_sekolah = data_dictionary.get("profil_sekolah")
            dispatcher.utter_message(text=f"{profil_sekolah}")
            return []

class ActionGetProdukSekolah(Action):
    def name(self) -> Text:
        return "action_produk_sekolah"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            produk_sekolah = data_dictionary.get("produk")
            dispatcher.utter_message(text=f"{produk_sekolah}")
            return []

# class ActionDefaultFallback(Action):
#     def name(self) -> Text:
#         return "action_default_fallback"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_default")
#         return []
