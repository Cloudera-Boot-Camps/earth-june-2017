drop table table_gravitational;

create table  table_gravitational
as
select a.detector_id,a.galaxy_id,a.amplitude_1,a.amplitude_2,a.amplitude_3, 
IF(a.amplitude_1 > 0.995 and a.amplitude_3>0.995 and a.amplitude_2 <0.005, 'Yes', 'No') as gravitational_wave from measurements a, detectors b, galaxies c
where a.detector_id=b.detector_id and a.galaxy_id=c.galaxy_id;


