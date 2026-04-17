## Archivo: occurrence.txt

Contiene los registros de observaciones de aves y especímenes preservados siguiendo el estándar Darwin Core.

### Atributos:

- **gbifID** Identificador único numérico asignado por GBIF a cada registro.
  *Ejemplo:* `1660908055`

- **accessRights** Información sobre los derechos de acceso o restricciones legales del dato.

- **bibliographicCitation** Referencia bibliográfica recomendada para citar el registro.

- **language** Idioma en el que se encuentra redactado el registro original.

- **license** Licencia legal bajo la cual se distribuye el dato.
  *Ejemplo:* `CC_BY_NC_4_0`

- **modified** Fecha y hora de la última modificación del registro digital.
  *Ejemplo:* `2015-05-19T00:00:00Z`

- **publisher** Nombre de la entidad u organización que publica la información.

- **references** Enlace web o identificador con información adicional sobre el registro.

- **rightsHolder** Persona o institución que posee los derechos sobre el registro.

- **type** Naturaleza del recurso del que se trata el registro.

- **institutionID** Identificador único para la institución de origen.

- **collectionID** Identificador único para la colección biológica.

- **datasetID** Identificador único para el conjunto de datos.

- **institutionCode** Siglas o código que identifica a la institución responsable.
  *Ejemplo:* `IADIZA`

- **collectionCode** Código que identifica la colección específica dentro de la institución.
  *Ejemplo:* `COI`

- **datasetName** Nombre formal del conjunto de datos al que pertenece la ocurrencia.

- **ownerInstitutionCode** Código de la institución dueña legal del objeto o espécimen.

- **basisOfRecord** Naturaleza del registro biológico.
  *Ejemplo:* `PRESERVED_SPECIMEN`

- **informationWithheld** Información omitida del registro público por razones de seguridad.

- **dataGeneralizations** Acciones de generalización aplicadas a los datos originales.

- **dynamicProperties** Lista de atributos adicionales que no tienen un campo estándar.

- **occurrenceID** Identificador único para la ocurrencia específica.

- **catalogNumber** Identificador único del ejemplar dentro del catálogo de la colección.
  *Ejemplo:* `IADIZA:COI:006861`

- **recordNumber** Número asignado por el colector al momento del hallazgo.
  *Ejemplo:* `006861`

- **recordedBy** Nombre de la persona o grupo que recolectó el dato original.
  *Ejemplo:* `R.G. Spurr`

- **recordedByID** Identificador persistente del colector u observador.

- **individualCount** Número de individuos presentes en la ocurrencia registrada.

- **organismQuantity** Valor de la cantidad medida de organismos.

- **organismQuantityType** Tipo de unidad utilizado para la cantidad medida.

- **sex** Sexo del individuo o individuos registrados.

- **lifeStage** Etapa del ciclo de vida del organismo.

- **reproductiveCondition** Estado reproductivo observado durante el registro.

- **caste** Casta social del individuo.

- **behavior** Comportamiento observado del individuo al momento del registro.

- **vitality** Estado de salud o vitalidad del organismo cuando se registró.

- **establishmentMeans** Proceso por el cual el organismo llegó a estar presente en la localidad.

- **degreeOfEstablishment** Grado en que una población introducida se ha establecido.

- **pathway** Mecanismo por el cual el organismo fue introducido en el sitio.

- **georeferenceVerificationStatus** Estado de la verificación de las coordenadas espaciales.

- **occurrenceStatus** Indica si el taxón estaba presente o ausente en el evento.
  *Ejemplo:* `PRESENT`

- **preparations** Lista de preparaciones físicas del espécimen.

- **disposition** Estado o ubicación actual del ejemplar físico.

- **associatedOccurrences** Ocurrencias relacionadas con este registro.

- **associatedReferences** Referencias bibliográficas relacionadas con el registro.

- **associatedSequences** Secuencias genéticas vinculadas al ejemplar.

- **associatedTaxa** Otros taxones registrados en asociación.

- **otherCatalogNumbers** Otros números de identificación que el ejemplar ha tenido.

- **occurrenceRemarks** Comentarios adicionales sobre la ocurrencia.

- **organismID** Identificador único para el organismo individual.

- **organismName** Nombre asignado al individuo.

- **organismScope** Alcance de la descripción del organismo.

- **associatedOrganisms** Otros organismos vinculados con el mismo registro.

- **previousIdentifications** Nombres científicos aplicados anteriormente al registro.

- **organismRemarks** Comentarios específicos sobre el organismo individual.

- **materialEntityID** Identificador de la entidad física o material biológico.

- **materialEntityRemarks** Notas sobre el material físico.

- **verbatimLabel** Transcripción textual completa de la etiqueta original.

- **materialSampleID** Identificador único para la muestra de material biológico.

- **eventID** Identificador del evento de muestreo.

- **parentEventID** Identificador del evento de nivel superior.

- **eventType** Tipo de evento registrado.

- **fieldNumber** Número de identificación dado al evento en el campo.

- **eventDate** Fecha en la que ocurrió el evento de registro.

- **eventTime** Hora en la que se realizó el registro.

- **startDayOfYear** Día inicial del año en que ocurrió el evento.

- **endDayOfYear** Día final del año en que ocurrió el evento.

- **year** Año numérico del registro.

- **month** Mes numérico del registro.

- **day** Día numérico del registro.

- **verbatimEventDate** Fecha del evento tal cual se anotó originalmente.

- **habitat** Descripción del ambiente donde se encontró el organismo.

- **samplingProtocol** Método utilizado para realizar el muestreo.

- **sampleSizeValue** Valor numérico del tamaño de la muestra.

- **sampleSizeUnit** Unidad de medida del tamaño de la muestra.

- **samplingEffort** Tiempo o intensidad dedicada al muestreo.

- **fieldNotes** Notas tomadas durante el trabajo de campo.

- **eventRemarks** Comentarios generales sobre el evento de muestreo.

- **locationID** Identificador único de la ubicación geográfica.

- **higherGeographyID** Identificador de la jerarquía geográfica superior.

- **higherGeography** Nombres de la jerarquía geográfica superior.

- **continent** Nombre del continente donde ocurrió el registro.
  *Ejemplo:* `SOUTH_AMERICA`

- **waterBody** Nombre del cuerpo de agua asociado al registro.

- **islandGroup** Nombre del grupo de islas o archipiélago.

- **island** Nombre de la isla específica.

- **countryCode** Código del país según el estándar ISO de dos letras.
  *Ejemplo:* `AR`

- **stateProvince** Nombre de la provincia o estado administrativo mayor.
  *Ejemplo:* `Río Negro`

- **county** División administrativa menor como departamento o condado.
  *Ejemplo:* `Pilcaniyeu`

- **municipality** Nombre del municipio o ciudad.

- **locality** Descripción de la localidad específica del hallazgo.
  *Ejemplo:* `Lago Los Juncos, Est. Perito Moreno 900m`

- **verbatimLocality** Descripción original de la localidad sin procesar.

- **verbatimElevation** Elevación original registrada en formato texto.

- **verticalDatum** Sistema de referencia utilizado para la elevación.

- **verbatimDepth** Profundidad original registrada.

- **minimumDistanceAboveSurfaceInMeters** Distancia mínima sobre la superficie terrestre.

- **maximumDistanceAboveSurfaceInMeters** Distancia máxima sobre la superficie terrestre.

- **locationAccordingTo** Fuente en la que se basa la descripción de la ubicación.

- **locationRemarks** Notas adicionales sobre la ubicación o el sitio.

- **decimalLatitude** Latitud geográfica expresada en grados decimales.

- **decimalLongitude** Longitud geográfica expresada en grados decimales.

- **coordinateUncertaintyInMeters** Radio de incertidumbre de la ubicación en metros.

- **coordinatePrecision** Precisión decimal de las coordenadas.

- **pointRadiusSpatialFit** Medida de ajuste espacial del punto geográfico.

- **verbatimCoordinates** Coordenadas tal cual se registraron originalmente.

- **verbatimLatitude** Latitud original sin procesar.

- **verbatimLongitude** Longitud original sin procesar.

- **verbatimCoordinateSystem** Sistema de coordenadas original de los datos.

- **verbatimSRS** Sistema de referencia espacial original.

- **footprintWKT** Geometría de la ubicación en formato de texto bien conocido.

- **footprintSRS** Sistema de referencia espacial para la geometría.

- **footprintSpatialFit** Ajuste espacial de la geometría definida.

- **georeferencedBy** Nombre de la persona que realizó la georreferenciación.

- **georeferencedDate** Fecha en la que se realizó la georreferenciación.

- **georeferenceProtocol** Método utilizado para obtener las coordenadas.

- **georeferenceSources** Fuentes utilizadas para la georreferenciación.

- **georeferenceRemarks** Notas sobre el proceso de obtención de coordenadas.

- **geologicalContextID** Identificador del contexto geológico para registros fósiles.

- **earliestEonOrLowestEonothem** Eón más antiguo asociado al registro.

- **latestEonOrHighestEonothem** Eón más reciente asociado al registro.

- **earliestEraOrLowestErathem** Era geológica asociada.

- **latestEraOrHighestErathem** Era geológica más reciente.

- **earliestPeriodOrLowestSystem** Periodo geológico asociado.

- **latestPeriodOrHighestSystem** Periodo geológico más reciente.

- **earliestEpochOrLowestSeries** Época geológica asociada.

- **latestEpochOrHighestSeries** Época geológica más reciente.

- **earliestAgeOrLowestStage** Edad geológica asociada.

- **latestAgeOrHighestStage** Edad geológica más reciente.

- **lowestBiostratigraphicZone** Zona bioestratigráfica más baja.

- **highestBiostratigraphicZone** Zona bioestratigráfica más alta.

- **lithostratigraphicTerms** Términos litoestratigráficos asociados.

- **group** Grupo litoestratigráfico.

- **formation** Formación geológica donde se encontró el registro.

- **member** Miembro de la formación geológica.

- **bed** Estrato o lecho geológico específico.

- **identificationID** Identificador único de la identificación taxonómica.

- **verbatimIdentification** Nombre científico tal cual se identificó originalmente.

- **identificationQualifier** Calificador que indica duda en la identificación.

- **typeStatus** Indica si el ejemplar es un tipo nomenclatural.

- **identifiedBy** Nombre de la persona que realizó la determinación taxonómica.

- **identifiedByID** Identificador de la persona que identificó el registro.

- **dateIdentified** Fecha en la que se realizó la identificación.

- **identificationReferences** Literatura utilizada para identificar el organismo.

- **identificationVerificationStatus** Nivel de seguridad de la identificación realizada.

- **identificationRemarks** Comentarios adicionales sobre la identificación.

- **taxonID** Identificador único del taxón en una base de datos.

- **scientificNameID** Identificador del nombre científico en un catálogo.

- **acceptedNameUsageID** Identificador del nombre científico aceptado.

- **parentNameUsageID** Identificador del taxón superior inmediato.

- **originalNameUsageID** Identificador del nombre original o basónimo.

- **nameAccordingToID** Identificador de la fuente del nombre taxonómico.

- **namePublishedInID** Identificador de la publicación del nombre.

- **taxonConceptID** Identificador del concepto taxonómico aplicado.

- **scientificName** Nombre científico completo con autoría.
  *Ejemplo:* `Chloephaga picta (J.F.Gmelin, 1789)`

- **acceptedNameUsage** Nombre científico que actualmente se considera válido.

- **parentNameUsage** Nombre del taxón superior en la jerarquía.

- **originalNameUsage** Nombre bajo el cual se describió originalmente el taxón.

- **nameAccordingTo** Referencia que respalda el uso del nombre científico.

- **namePublishedIn** Publicación original donde se describió el nombre.

- **namePublishedInYear** Año de publicación del nombre científico.

- **higherClassification** Cadena de texto con la jerarquía taxonómica completa.

- **kingdom** Reino biológico del taxón.
  *Ejemplo:* `Animalia`

- **phylum** Filo o división taxonómica.
  *Ejemplo:* `Chordata`

- **class** Clase taxonómica del ejemplar.
  *Ejemplo:* `Aves`

- **order** Orden taxonómico del organismo.
  *Ejemplo:* `Anseriformes`

- **superfamily** Superfamilia taxonómica.

- **family** Familia taxonómica del organismo.
  *Ejemplo:* `Anatidae`

- **subfamily** Subfamilia taxonómica.

- **tribe** Tribu taxonómica.

- **subtribe** Subtribu taxonómica.

- **genus** Género taxonómico del organismo.
  *Ejemplo:* `Chloephaga`

- **genericName** Parte genérica del nombre científico.
  *Ejemplo:* `Chloephaga`

- **subgenus** Subgénero taxonómico.

- **infragenericEpithet** Epíteto infragenérico del nombre.

- **specificEpithet** Epíteto específico del nombre científico.
  *Ejemplo:* `picta`

- **infraspecificEpithet** Epíteto subespecífico del nombre.

- **cultivarEpithet** Nombre asignado a una variedad cultivada.

- **taxonRank** Nivel jerárquico del nombre científico.
  *Ejemplo:* `SPECIES`

- **verbatimTaxonRank** Rango taxonómico tal cual se registró originalmente.

- **vernacularName** Nombre común o vulgar del organismo.

- **nomenclaturalCode** Código de nomenclatura que rige el nombre.

- **taxonomicStatus** Estado de validez taxonómica del nombre.
  *Ejemplo:* `ACCEPTED`

- **nomenclaturalStatus** Estatus del nombre según las reglas de nomenclatura.

- **taxonRemarks** Comentarios adicionales sobre la taxonomía del registro.

- **datasetKey** Identificador único del conjunto de datos en GBIF.
  *Ejemplo:* `a0d072fc-e6be-45d7-9fa8-afa4b38b788a`

- **publishingCountry** Código del país de la institución que publica los datos.
  *Ejemplo:* `AR`

- **lastInterpreted** Fecha de la última interpretación de datos por GBIF.
  *Ejemplo:* `2025-11-25T07:12:45.267Z`

- **elevation** Elevación interpretada en metros sobre el nivel del mar.

- **elevationAccuracy** Precisión estimada de la elevación en metros.

- **depth** Profundidad interpretada en metros bajo el nivel del mar.

- **depthAccuracy** Precisión estimada de la profundidad en metros.

- **distanceFromCentroidInMeters** Distancia al centroide geográfico en metros.

- **issue** Problemas de calidad de datos detectados durante el procesamiento.
  *Ejemplo:* `CONTINENT_DERIVED_FROM_COUNTRY`

- **mediaType** Tipos de archivos multimedia asociados al registro.

- **hasCoordinate** Indica si el registro posee coordenadas geográficas válidas.
  *Ejemplo:* `false`

- **hasGeospatialIssues** Indica si se detectaron problemas geoespaciales.
  *Ejemplo:* `false`

- **taxonKey** Clave numérica interna de GBIF para el taxón.
  *Ejemplo:* `5232428`

- **acceptedTaxonKey** Clave del taxón aceptado en el sistema de GBIF.
  *Ejemplo:* `5232428`

- **kingdomKey** Clave numérica de GBIF para el Reino.
  *Ejemplo:* `1`

- **phylumKey** Clave numérica de GBIF para el Filo.
  *Ejemplo:* `44`

- **classKey** Clave numérica de GBIF para la Clase.
  *Ejemplo:* `212`

- **orderKey** Clave numérica de GBIF para el Orden.
  *Ejemplo:* `1108`

- **familyKey** Clave numérica de GBIF para la Familia.
  *Ejemplo:* `2986`

- **genusKey** Clave numérica de GBIF para el Género.
  *Ejemplo:* `2497988`

- **subgenusKey** Clave numérica de GBIF para el Subgénero.

- **speciesKey** Clave numérica de GBIF para la Especie.
  *Ejemplo:* `5232428`

- **species** Nombre científico de la especie sin autoría.
  *Ejemplo:* `Chloephaga picta`

- **acceptedScientificName** Nombre científico aceptado con autoría completa.
  *Ejemplo:* `Chloephaga picta (J.F.Gmelin, 1789)`

- **verbatimScientificName** Nombre científico tal cual fue provisto originalmente.
  *Ejemplo:* `Chloephaga picta`

- **typifiedName** Nombre científico que es tipificado por este ejemplar.

- **protocol** Protocolo técnico utilizado para la transferencia de datos.
  *Ejemplo:* `EML`

- **lastParsed** Fecha del último análisis técnico del registro por GBIF.
  *Ejemplo:* `2025-11-25T07:12:45.267Z`

- **lastCrawled** Fecha de la última recolección del dato desde el origen.
  *Ejemplo:* `2025-11-24T06:34:24.956Z`

- **repatriated** Indica si el dato ha sido devuelto digitalmente a su país de origen.
  *Ejemplo:* `false`

- **relativeOrganismQuantity** Medida de abundancia relativa del organismo.

- **projectId** Identificador del proyecto de investigación asociado.

- **isSequenced** Indica si el ejemplar posee datos de secuencias de ADN.
  *Ejemplo:* `false`

- **gbifRegion** Región geográfica según la clasificación interna de GBIF.
  *Ejemplo:* `LATIN_AMERICA`

- **publishedByGbifRegion** Región de GBIF a la que pertenece la institución publicadora.
  *Ejemplo:* `LATIN_AMERICA`

- **level0Gid** Identificador del país en el nivel 0 de la base de datos geográfica.

- **level0Name** Nombre del país según la base de datos geográfica.

- **level1Gid** Identificador de la provincia en el nivel 1.

- **level1Name** Nombre de la provincia o estado administrativo.

- **level2Gid** Identificador de la división política menor en el nivel 2.

- **level2Name** Nombre del departamento o condado.

- **level3Gid** Identificador de la municipalidad en el nivel 3.

- **level3Name** Nombre de la municipalidad.

- **iucnRedListCategory** Categoría de conservación según la Lista Roja de la UICN.
  *Ejemplo:* `LC`